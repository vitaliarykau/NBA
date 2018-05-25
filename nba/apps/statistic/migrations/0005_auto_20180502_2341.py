# Generated by Django 2.0.4 on 2018-05-02 23:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_auto_20180430_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='match',
            name='score1',
            field=models.PositiveSmallIntegerField(default=50, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(170)], verbose_name='Home Team Scores'),
        ),
        migrations.AlterField(
            model_name='match',
            name='score2',
            field=models.PositiveSmallIntegerField(default=51, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(170)], verbose_name='Away Team Scores'),
        ),
    ]