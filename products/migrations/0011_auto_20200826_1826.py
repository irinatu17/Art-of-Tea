# Generated by Django 3.0.7 on 2020-08-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200824_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk']},
        ),
    ]
