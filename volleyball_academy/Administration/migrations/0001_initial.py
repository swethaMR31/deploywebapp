# Generated by Django 3.0.8 on 2020-08-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField(max_length=10)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('category', models.CharField(max_length=20)),
                ('parent_name', models.CharField(max_length=20)),
                ('mobile_no', models.BigIntegerField()),
                ('standard', models.CharField(max_length=20)),
                ('session', models.CharField(max_length=20)),
                ('doj', models.DateField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'candidate',
            },
        ),
    ]
