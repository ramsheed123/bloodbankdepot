# Generated by Django 4.2.1 on 2023-05-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0005_rename_corporation_registration_ward_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='ward_number',
        ),
        migrations.AddField(
            model_name='registration',
            name='ward_numbers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
