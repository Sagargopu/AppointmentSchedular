# Generated by Django 4.2.6 on 2023-11-01 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0004_appointment_day'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['Professor', 'Day', 'Date'], 'verbose_name_plural': 'Appointments'},
        ),
    ]
