# Generated by Django 2.0.4 on 2018-06-20 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_checkinuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinuser',
            name='workhours',
            field=models.TimeField(null=True, verbose_name='work_hours'),
        ),
        migrations.AlterField(
            model_name='checkinuser',
            name='punchin',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 18, 21, 50, tzinfo=utc), verbose_name='check_in'),
        ),
    ]
