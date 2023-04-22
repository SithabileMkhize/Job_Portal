# Generated by Django 4.2 on 2023-04-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('companyName', models.CharField(default='', max_length=50)),
                ('responsibilities', models.CharField(default='', max_length=150)),
                ('requirements', models.CharField(default='', max_length=150)),
            ],
        ),
    ]