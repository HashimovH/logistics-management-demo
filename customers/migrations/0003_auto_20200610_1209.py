# Generated by Django 2.2.3 on 2020-06-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200610_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
