# Generated by Django 4.0.6 on 2022-07-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]