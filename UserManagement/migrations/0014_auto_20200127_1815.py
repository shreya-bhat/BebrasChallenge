# Generated by Django 3.0 on 2020-01-27 12:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0013_auto_20200127_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_user',
            name='modified_on',
            field=models.DateField(default=datetime.datetime(2020, 1, 27, 12, 45, 17, 401036, tzinfo=utc)),
        ),
    ]
