# Generated by Django 2.2.3 on 2020-06-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200612_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qaime_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]