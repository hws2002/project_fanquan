# Generated by Django 3.2.15 on 2023-07-20 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('event_name', models.CharField(db_column='event_name', default='', max_length=128, unique=True)),
                ('event_description', models.CharField(db_column='event_description', max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('capacity', models.IntegerField(db_column='capacity')),
                ('joined', models.IntegerField(db_column='joined', default=1)),
                ('category_id', models.ForeignKey(db_column='category_id', default='1', on_delete=django.db.models.deletion.PROTECT, to='event_hall.category')),
                ('host_id', models.ForeignKey(db_column='host_id', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hosted_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.CASCADE, to='event_hall.event')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
