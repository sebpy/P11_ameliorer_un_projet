# Generated by Django 2.2.4 on 2019-09-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20190904_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id_categories',
            field=models.SmallIntegerField(default=0),
        ),
    ]
