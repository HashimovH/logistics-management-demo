# Generated by Django 2.2.3 on 2020-06-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_notification_where'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
