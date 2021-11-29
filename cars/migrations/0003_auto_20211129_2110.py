# Generated by Django 3.2.9 on 2021-11-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20211129_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carstats',
            name='acceleration400',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Acceleration time from 0 to 400 meters', null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='acceleration_0_100',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='acceleration_100_200',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='fuel_tank_capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Car height in cm', null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='length',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Car length in cm', null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='max_boot_capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='min_boot_capacity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='num_of_doors',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='num_of_seats',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='nurburgring_lap_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='turning_radius',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='v_max',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Car width in cm', null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='year_of_end_production',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carstats',
            name='year_of_start_production',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]