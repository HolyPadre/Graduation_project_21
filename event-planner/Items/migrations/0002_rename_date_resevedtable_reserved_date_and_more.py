# Generated by Django 4.0.3 on 2022-06-27 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resevedtable',
            old_name='Date',
            new_name='reserved_date',
        ),
        migrations.RemoveField(
            model_name='resevedtable',
            name='event',
        ),
    ]
