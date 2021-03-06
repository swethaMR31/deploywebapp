# Generated by Django 3.0.8 on 2020-08-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0005_player_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='session',
        ),
        migrations.AddField(
            model_name='coach',
            name='gender',
            field=models.CharField(choices=[('a', 'Male'), ('b', 'Female')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='standard',
            field=models.CharField(choices=[('a', 'Beginner'), ('b', 'Intermediate'), ('c', 'Advanced')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='dob',
            field=models.DateField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('a', 'Male'), ('b', 'Female')], max_length=25, null=True),
        ),
    ]
