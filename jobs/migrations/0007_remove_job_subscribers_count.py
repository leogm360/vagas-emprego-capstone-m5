# Generated by Django 4.0.6 on 2022-07-15 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_job_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='subscribers_count',
        ),
    ]
