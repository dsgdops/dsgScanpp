# Generated by Django 4.0.2 on 2022-02-21 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0003_rename_scans_scan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='scan',
        ),
    ]
