# Generated by Django 4.1.5 on 2023-01-17 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_queuedurable_is_borrowed_queueparcel_is_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandurable',
            name='idcart',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cartdurable'),
        ),
        migrations.AddField(
            model_name='loanparcel',
            name='idcart',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cartparcel'),
        ),
    ]
