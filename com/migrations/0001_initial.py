# Generated by Django 3.0 on 2020-01-27 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressID', models.AutoField(db_column='AddressID', primary_key=True, serialize=False)),
                ('line1', models.TextField(db_column='Line1')),
                ('line2', models.TextField(db_column='Line2')),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='code',
            fields=[
                ('codeID', models.AutoField(db_column='codeID', primary_key=True, serialize=False)),
                ('codeName', models.CharField(db_column='codeName', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='codeGroup',
            fields=[
                ('codeGroupID', models.AutoField(db_column='codeGroupID', primary_key=True, serialize=False)),
                ('codeGroupName', models.CharField(db_column='codeGroupName', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('countryID', models.AutoField(primary_key=True, serialize=False)),
                ('iso', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=80)),
                ('nicename', models.CharField(max_length=80)),
                ('iso3', models.CharField(blank=True, max_length=3, null=True)),
                ('numcode', models.SmallIntegerField(blank=True, null=True)),
                ('phonecode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('schoolID', models.AutoField(db_column='schoolID', primary_key=True, serialize=False)),
                ('schoolName', models.CharField(db_column='schoolName', max_length=100)),
                ('UDISEcode', models.CharField(max_length=15)),
                ('tag', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('addressID', models.ForeignKey(db_column='addressID', on_delete=django.db.models.deletion.CASCADE, to='com.Address')),
                ('schoolTypeCodeID', models.ForeignKey(db_column='schoolTypeCodeID', on_delete=django.db.models.deletion.CASCADE, to='com.code')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('stateID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('countryID', models.ForeignKey(db_column='countryID', on_delete=django.db.models.deletion.CASCADE, to='com.Countries')),
            ],
        ),
        migrations.CreateModel(
            name='schoolClass',
            fields=[
                ('schoolClassID', models.AutoField(db_column='schoolClassID', primary_key=True, serialize=False)),
                ('classNumber', models.IntegerField(db_column='classNumber')),
                ('schoolID', models.ForeignKey(db_column='schoolID', on_delete=django.db.models.deletion.CASCADE, to='com.school')),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('districtID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('stateID', models.ForeignKey(db_column='stateID', on_delete=django.db.models.deletion.CASCADE, to='com.States')),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='codeGroupID',
            field=models.ForeignKey(db_column='codeGroupID', on_delete=django.db.models.deletion.CASCADE, to='com.codeGroup'),
        ),
        migrations.AddField(
            model_name='address',
            name='countryID',
            field=models.ForeignKey(db_column='countryID', on_delete=django.db.models.deletion.CASCADE, to='com.Countries'),
        ),
        migrations.AddField(
            model_name='address',
            name='districtID',
            field=models.ForeignKey(db_column='districtID', on_delete=django.db.models.deletion.CASCADE, to='com.Districts'),
        ),
        migrations.AddField(
            model_name='address',
            name='stateID',
            field=models.ForeignKey(db_column='stateID', on_delete=django.db.models.deletion.CASCADE, to='com.States'),
        ),
    ]
