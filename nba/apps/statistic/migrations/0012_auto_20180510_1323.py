# Generated by Django 2.0.4 on 2018-05-10 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0011_auto_20180510_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 10, 13, 23, 3, 488507, tzinfo=utc), verbose_name='Date and Time'),
        ),
    ]
