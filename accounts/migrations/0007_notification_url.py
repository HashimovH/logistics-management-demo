# Generated by Django 2.2.3 on 2020-06-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_notification_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
