# Generated by Django 3.0 on 2020-01-26 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0008_auto_20200125_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_user',
            name='modified_on',
            field=models.DateField(default=datetime.datetime(2020, 1, 26, 11, 22, 13, 806480, tzinfo=utc)),
        ),
    ]
