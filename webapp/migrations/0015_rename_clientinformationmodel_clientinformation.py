# Generated by Django 4.1.7 on 2023-12-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_clientinformationmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientInformationModel',
            new_name='ClientInformation',
        ),
    ]
