# Generated by Django 2.0.4 on 2018-05-23 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0022_auto_20180523_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name_plural': 'Coaches'},
        ),
        migrations.AlterField(
            model_name='coach',
            name='b_day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='statistic.Team', unique=True),
        ),
    ]
