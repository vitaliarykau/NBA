# Generated by Django 2.0.4 on 2018-05-09 23:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0008_auto_20180509_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'permissions': (('can_moderate', 'Moderate data in app statistic'),), 'verbose_name_plural': 'matches'},
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 9, 23, 1, 21, 214226, tzinfo=utc), verbose_name='Date and Time'),
        ),
    ]
