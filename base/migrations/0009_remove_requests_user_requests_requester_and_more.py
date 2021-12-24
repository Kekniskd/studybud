# Generated by Django 4.0 on 2021-12-24 09:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_requests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='user',
        ),
        migrations.AddField(
            model_name='requests',
            name='requester',
            field=models.ManyToManyField(blank=True, related_name='requester', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]