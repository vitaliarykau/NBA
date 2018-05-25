# Generated by Django 2.0.4 on 2018-05-23 21:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0018_auto_20180522_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='stat',
            name='match',
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='College name'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='statistic.Team', verbose_name='Home Team'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statistic.Player'),
        ),
        migrations.AlterField(
            model_name='stat',
            name='rebounds',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='stat',
            name='season',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.PROTECT, to='statistic.Season'),
            preserve_default=False,
        ),
    ]
