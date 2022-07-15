# Generated by Django 4.0.6 on 2022-07-14 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('companies', '0002_remove_company_adress_company_address'),
        ('accounts', '0002_rename_is_recruiter_account_is_human_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='addresses.address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='companies.company'),
        ),
    ]
