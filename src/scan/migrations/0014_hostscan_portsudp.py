# Generated by Django 4.0.2 on 2022-03-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0013_remove_hostscan_portsudp'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostscan',
            name='portsUDP',
            field=models.JSONField(default=[]),
        ),
    ]
