# Generated by Django 3.2 on 2021-04-25 12:50

from django.core import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_review_test_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='course_load',
            field=models.SmallIntegerField(
                validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.SmallIntegerField(
                validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)]),
        ),
    ]
