# Generated by Django 2.2.3 on 2020-06-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_vehicle_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type_car',
            field=models.CharField(choices=[('Evakuator', 'Evakuator'), ('Refrigerator', 'Refrigerator')], max_length=255),
        ),
    ]