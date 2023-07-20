# Generated by Django 3.2.15 on 2023-07-20 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_hall', '0002_alter_userevent_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', default='1', on_delete=django.db.models.deletion.PROTECT, related_name='events', to='event_hall.category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='host_id',
            field=models.ForeignKey(db_column='host_id', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hosting_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='event_id',
            field=models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.CASCADE, related_name='event_members', to='event_hall.event'),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to=settings.AUTH_USER_MODEL),
        ),
    ]