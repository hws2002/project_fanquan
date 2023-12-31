# Generated by Django 3.2.15 on 2023-07-20 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='friend_id',
            field=models.ForeignKey(db_column='friend_id', on_delete=django.db.models.deletion.CASCADE, related_name='friend_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_friend', to=settings.AUTH_USER_MODEL),
        ),
    ]
