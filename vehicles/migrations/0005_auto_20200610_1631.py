# Generated by Django 2.2.3 on 2020-06-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20200610_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Free', 'Free')], default='Free', max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type_car',
            field=models.CharField(choices=[('Evakuator', 'Evakuator')], max_length=255),
        ),
    ]
