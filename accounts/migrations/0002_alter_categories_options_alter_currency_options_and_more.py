# Generated by Django 4.1 on 2022-08-05 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transactions'},
        ),
    ]
