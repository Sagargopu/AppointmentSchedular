# Generated by Django 4.2.6 on 2023-11-09 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0012_appointment_created_by_appointment_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['Date', 'Time', 'Professor', 'Day'], 'verbose_name_plural': 'Appointments'},
        ),
    ]