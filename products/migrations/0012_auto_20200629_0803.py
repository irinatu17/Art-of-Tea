# Generated by Django 3.0.7 on 2020-06-29 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200629_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='text',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='time',
        ),
    ]