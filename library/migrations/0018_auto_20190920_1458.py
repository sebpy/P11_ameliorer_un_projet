# Generated by Django 2.2.4 on 2019-09-20 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20190920_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersaveproduct',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='usersaveproduct',
            old_name='user',
            new_name='user_id',
        ),
    ]