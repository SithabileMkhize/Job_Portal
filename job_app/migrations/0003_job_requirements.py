# Generated by Django 4.2 on 2023-04-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0002_job_delete_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(default='Matric', max_length=150),
            preserve_default=False,
        ),
    ]
