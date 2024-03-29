# Generated by Django 2.2.3 on 2020-06-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='destination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Credit Card', 'Credit Card')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='start',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
