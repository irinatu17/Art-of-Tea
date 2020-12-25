# Generated by Django 3.0.7 on 2020-07-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_orderitemdetails_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='orderitemdetails',
            name='datetime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
