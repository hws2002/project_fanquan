# Generated by Django 3.2.15 on 2023-07-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_column='name', max_length=128),
        ),
    ]
