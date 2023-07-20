# Generated by Django 3.2.15 on 2023-07-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_hall', '0003_auto_20230720_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Sports'), ('2', 'Lecture'), ('3', 'Concert'), ('4', 'Hangout'), ('5', 'Study'), ('6', 'School Event'), ('7', 'others')], db_column='name', default='', max_length=128, unique=True),
        ),
    ]