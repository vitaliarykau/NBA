# Generated by Django 2.0.4 on 2018-05-23 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0021_auto_20180523_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('b_day', models.TimeField()),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='statistic.Team')),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
