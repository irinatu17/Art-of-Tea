# Generated by Django 3.0.7 on 2020-06-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200627_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='text',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='time',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
