# Generated by Django 3.2.5 on 2021-07-14 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student',
        ),
        migrations.AddField(
            model_name='admin',
            name='Bdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 14, 19, 48, 8, 265340, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='Role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student')], default='admin', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='Bdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 14, 19, 48, 29, 86219, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student')], default='student', max_length=10),
        ),
    ]
