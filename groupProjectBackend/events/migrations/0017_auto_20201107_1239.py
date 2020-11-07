# Generated by Django 3.0.8 on 2020-11-07 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20201105_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='event_datetime_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_start',
        ),
        migrations.AddField(
            model_name='event',
            name='event_datetime_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]