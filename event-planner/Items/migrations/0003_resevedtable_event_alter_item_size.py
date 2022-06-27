# Generated by Django 4.0.3 on 2022-06-27 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('Items', '0002_rename_date_resevedtable_reserved_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resevedtable',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.IntegerField(default=100),
        ),
    ]
