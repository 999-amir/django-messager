# Generated by Django 5.1 on 2024-08-20 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumeuser',
            name='is_verify',
        ),
    ]
