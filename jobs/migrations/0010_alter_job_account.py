# Generated by Django 4.0.6 on 2022-07-20 00:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0009_alter_job_options_alter_job_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='account',
            field=models.ManyToManyField(related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]