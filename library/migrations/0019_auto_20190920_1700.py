# Generated by Django 2.2.4 on 2019-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20190920_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersaveproduct',
            name='product_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.Product'),
        ),
    ]
