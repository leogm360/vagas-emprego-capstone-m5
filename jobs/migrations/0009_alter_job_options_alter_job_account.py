# Generated by Django 4.0.6 on 2022-07-20 00:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0008_alter_job_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='job',
            name='account',
            field=models.ManyToManyField(related_name='accounts_job', to=settings.AUTH_USER_MODEL),
        ),
    ]
