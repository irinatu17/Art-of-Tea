# Generated by Django 3.0.7 on 2020-06-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200628_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='name',
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]