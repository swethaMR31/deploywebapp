# Generated by Django 3.0.8 on 2020-08-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0004_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
