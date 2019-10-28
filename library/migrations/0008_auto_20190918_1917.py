# Generated by Django 2.2.4 on 2019-09-18 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20190904_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=250)),
                ('nutriscore_product', models.CharField(max_length=1)),
                ('fat_100g', models.CharField(blank=True, max_length=10)),
                ('sugars_100g', models.CharField(blank=True, max_length=10)),
                ('saturated_fat_100g', models.CharField(blank=True, max_length=10)),
                ('salt_100g', models.CharField(blank=True, max_length=20)),
                ('image_product', models.URLField(blank=True)),
                ('link_product', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='usersaveproduct',
            name='save_product',
        ),
        migrations.AlterField(
            model_name='usersaveproduct',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Product'),
        ),
        migrations.AlterField(
            model_name='usersaveproduct',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameModel(
            old_name='ProductCategories',
            new_name='ProductCategorie',
        ),
        migrations.AddField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.ProductCategorie'),
        ),
    ]
