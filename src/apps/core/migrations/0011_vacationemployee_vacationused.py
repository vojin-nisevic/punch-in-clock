# Generated by Django 2.0.4 on 2018-05-31 20:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180521_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacation_days', models.PositiveIntegerField(default=25, validators=[django.core.validators.MaxValueValidator(50)], verbose_name='vacation_days')),
                ('vacation_remainder', models.PositiveIntegerField(default=0, verbose_name='vacation_remainder')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vacation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VacationUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_vacation', models.DateField(unique_for_date=True, verbose_name='start_vacation')),
                ('end_vacation', models.DateField(unique_for_date=True, verbose_name='end_vacation')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacation_used', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]