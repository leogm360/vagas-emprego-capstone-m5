# Generated by Django 4.0.6 on 2022-07-20 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_alter_skill_options'),
        ('jobs', '0010_alter_job_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='skills.skill'),
        ),
    ]
