# Generated by Django 3.0.8 on 2020-08-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0003_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('dob', models.DateField(max_length=10)),
                ('experience', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
                ('session', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('DOJ', models.DateTimeField(auto_now_add=True, verbose_name='doj')),
            ],
        ),
    ]