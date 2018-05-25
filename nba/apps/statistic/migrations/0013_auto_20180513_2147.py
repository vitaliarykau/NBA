# Generated by Django 2.0.4 on 2018-05-13 21:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0012_auto_20180510_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'permissions': (('statistic.can_moderate', 'Moderate data in app statistic'),)},
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 13, 21, 47, 47, 365241, tzinfo=utc), verbose_name='Date and Time'),
        ),
    ]