# Generated by Django 4.1.5 on 2023-01-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_loandurable_idcart_loanparcel_idcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loandurable',
            name='idcart',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='loanparcel',
            name='idcart',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
