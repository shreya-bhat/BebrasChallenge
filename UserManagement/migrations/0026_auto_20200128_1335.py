# Generated by Django 3.0 on 2020-01-28 08:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0025_auto_20200128_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_user',
            name='modified_on',
            field=models.DateField(default=datetime.datetime(2020, 1, 28, 8, 5, 12, 759592, tzinfo=utc)),
        ),
    ]
