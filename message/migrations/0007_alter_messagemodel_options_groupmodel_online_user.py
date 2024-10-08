# Generated by Django 5.1 on 2024-08-22 14:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_alter_groupmodel_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messagemodel',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='online_user',
            field=models.ManyToManyField(blank=True, related_name='rel_online_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
