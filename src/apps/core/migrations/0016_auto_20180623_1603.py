# Generated by Django 2.0.4 on 2018-06-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180620_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinuser',
            name='punchin',
            field=models.DateTimeField(null=True, verbose_name='check_in'),
        ),
    ]
