# Generated by Django 2.2.4 on 2019-09-20 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20190919_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersaveproduct',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Product', unique=True),
        ),
    ]