# Generated by Django 2.2.16 on 2022-02-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220201_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(help_text='Дата публикации', verbose_name='Дата публикации'),
        ),
    ]