# Generated by Django 2.2.4 on 2019-09-19 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20190919_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersaveproduct',
            name='id_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]