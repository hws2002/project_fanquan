# Generated by Django 3.2.15 on 2023-07-21 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20230721_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(db_column='user_type', default=3, on_delete=django.db.models.deletion.CASCADE, to='dashboard.usertype'),
        ),
    ]