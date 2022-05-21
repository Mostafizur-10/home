# Generated by Django 4.0.2 on 2022-04-26 18:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_plot_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='area',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='latitude',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AddField(
            model_name='plot',
            name='longitude',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
    ]
