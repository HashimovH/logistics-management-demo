# Generated by Django 2.2.3 on 2020-06-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
