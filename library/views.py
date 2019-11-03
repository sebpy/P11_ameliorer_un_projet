""" View file for module Library """

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Product, UserSaveProduct
from .forms import LoginForm, RegisterForm


def index(request):
    """ Display index """
    return render(request, 'library/index.html')


def legal_notice(request):
    """ Display legal Notice """
    return render(request, 'library/legal-notice.html')


def detail(request, product_id):
    """ Display detail product """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'name_product': product.name_product,
        'nutriscore_product': product.nutriscore_product,
        'fat_100g': product.fat_100g,
        'sugars_100g': product.sugars_100g,
        'saturated_fat_100g': product.saturated_fat_100g,
        'salt_100g': product.salt_100g,
        'image_product': product.image_product,
        'link_product': product.link_product
    }
    return render(request, 'library/detail.html', context)


def search(request):
    """ Display search product """
    query = request.GET.get('query', '')
    if not query:
        messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                '</i> ERREUR!</strong><br>'
                                'Vous devez entrer un aliment à rechercher.', extra_tags='safe')

        return render(request, 'library/index.html')

    if query:
        products = Product.objects.filter(name_product__icontains=query)\
            .order_by('nutriscore_product')

        paginator = Paginator(products, 9)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            'products': products,
            'query': query,
            'paginate': True
        }
        return render(request, 'library/search.html', context)


def login_page(request):
    """ Display login page """
    form_login = LoginForm()
    context = {
        "formLogin": form_login,
    }
    return render(request, 'library/login.html', context)


def login_user(request):
    """ Function for user login """
    form_login = LoginForm()
    context = {
        "formLogin": form_login,
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, '<strong><i class="fas fa-exclamation-triangle">'
                                          '</i> Succès!</strong><br>'
                                          'Vous êtes connecté avec succès.', extra_tags='safe')

                context = {
                    "username": request.user.username,
                    "email": request.user.email,
                }
                return render(request, 'library/profile.html', context)

            if not user:
                messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                        '</i> Erreur!</strong><br>'
                                        'Login ou mot de passe invalide.', extra_tags='safe')

                return render(request, 'library/login.html', context)
    else:
        return render(request, 'library/login.html', context)


def logout_user(request):
    """ Function for user logout """
    logout(request)
    messages.success(request, '<strong><i class="fas fa-exclamation-triangle">'
                              '</i> Succès!</strong><br>'
                              'Vous avez été déconnecté avec succès.', extra_tags='safe')

    return render(request, 'library/index.html')


@login_required
def profile(request):
    """ Display User profile """
    context = {
        "username": request.user.username,
        "email": request.user.email,
    }
    return render(request, 'library/profile.html', context)


def register(request):
    """ Function for register """
    form_register = RegisterForm()
    context = {
        "formRegister": form_register
    }
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                email = form.cleaned_data.get('email')
                if password2 != password1:
                    messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                            '</i> Erreur!</strong><br>'
                                            'Les mot de passe sont différent', extra_tags='safe')
                else:
                    User.objects.create_user(username=username,
                                             email=email,
                                             password=password1)

                    user = authenticate(request, username=username, password=password1)
                    if user:
                        login(request, user)

                        context = {
                            "username": request.user.username,
                            "email": request.user.email,
                        }
                        return render(request, 'library/profile.html', context)
                    if not user:
                        messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                                '</i> Erreur!</strong><br>'
                                                'Vous devez remplir tous les champs.',
                                       extra_tags='safe')

        else:
            return render(request, 'library/register.html', context)

    except IntegrityError:
        messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                '</i> Erreur!</strong><br>'
                                'Cette utilisateur existe déjà.', extra_tags='safe')

        return render(request, 'library/register.html', context)

    return render(request, 'library/register.html', context)


@login_required
def save_product(request):
    """ Function for save product """
    product_id = request.GET.get('id')
    product = get_object_or_404(Product, pk=product_id)
    user = request.user.id
    save_user = get_object_or_404(User, pk=user)
    try:
        save = UserSaveProduct.objects.create(
            user_id=save_user,
            product_id=product
        )
        save.save()

    except Exception as ex:
        print(str(ex))
        msg = "\n\nInsertion error"
        print(msg)

    context = {
        'name_product': product.name_product,
        'nutriscore_product': product.nutriscore_product,
        'fat_100g': product.fat_100g,
        'sugars_100g': product.sugars_100g,
        'saturated_fat_100g': product.saturated_fat_100g,
        'salt_100g': product.salt_100g,
        'image_product': product.image_product,
        'link_product': product.link_product
    }
    return render(request, 'library/save.html', context)


@login_required
def read_user_list(request):
    """ Function for display saved products for current user """

    profile_id = request.user.id
    query = UserSaveProduct.objects.filter(user_id=profile_id)

    if not query:
        messages.error(request, '<strong><i class="fas fa-exclamation-triangle">'
                                '</i> ERREUR!</strong><br>'
                                'Vous n\'avez sauvegardé aucun aliment.', extra_tags='safe')

        return render(request, 'library/index.html')

    if query:
        context = {
            'products': query,
        }
        return render(request, 'library/saved.html', context)


@login_required
def delete_saved(request):
    """ Function for display saved products for current user """

    del_id = request.GET.get('id')
    try:
        delete = UserSaveProduct.objects.get(pk=del_id)
        delete.delete()

        messages.success(request, '<strong><i class="fas fa-exclamation-triangle">'
                                  '</i> Succès!</strong><br>'
                                  'Aliment supprimé avec succès.', extra_tags='safe')

    except Exception as ex:
        print(str(ex))
        msg = "\n\nDelete error"
        print(msg)

    return redirect('/library/saved/')

