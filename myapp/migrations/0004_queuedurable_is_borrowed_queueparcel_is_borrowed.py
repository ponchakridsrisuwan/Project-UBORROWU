# Generated by Django 4.1.5 on 2023-01-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_listfromrec_reasonfromstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='queuedurable',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='queueparcel',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
    ]