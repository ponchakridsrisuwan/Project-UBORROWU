# Generated by Django 4.1.5 on 2023-01-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_username_listfromrec_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listfromrec',
            name='reasonfromstaff',
            field=models.TextField(default='', max_length=500),
        ),
    ]
