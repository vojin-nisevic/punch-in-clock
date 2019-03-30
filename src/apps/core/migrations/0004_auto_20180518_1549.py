# Generated by Django 2.0.4 on 2018-05-18 15:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180306_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('type', models.CharField(choices=[('AD', 'Administrative days'), ('FC', 'Family care days'), ('FU', 'Funeral days')], max_length=2, verbose_name='type')),
                ('duration', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10, 'Cannot be greater then 10'), django.core.validators.MinValueValidator(0, 'Cannot be less then zero')], verbose_name='duration')),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('holiday_type', models.CharField(choices=[('N', 'National'), ('L', 'Local'), ('R', 'Religious')], max_length=1, verbose_name='type')),
                ('date', models.DateField(unique=True, verbose_name='date')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]