# Generated by Django 3.0 on 2020-01-27 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0022_auto_20200127_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_user',
            name='modified_on',
            field=models.DateField(default=datetime.datetime(2020, 1, 27, 13, 29, 8, 910589, tzinfo=utc)),
        ),
    ]
