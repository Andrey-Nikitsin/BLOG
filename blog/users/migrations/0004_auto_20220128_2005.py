# Generated by Django 3.2.8 on 2022-01-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_clients_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelTable(
            name='clients',
            table='clients',
        ),
    ]
