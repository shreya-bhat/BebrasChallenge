# Generated by Django 3.0 on 2020-01-26 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0009_auto_20200126_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usr_user',
            name='modified_on',
            field=models.DateField(default=datetime.datetime(2020, 1, 26, 12, 14, 55, 34126, tzinfo=utc)),
        ),
    ]
