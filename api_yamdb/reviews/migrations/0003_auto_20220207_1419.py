# Generated by Django 2.2.16 on 2022-02-07 11:19

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220206_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(help_text='Год выпуска', validators=[reviews.validators.validate_year], verbose_name='Год выпуска'),
        ),
    ]
