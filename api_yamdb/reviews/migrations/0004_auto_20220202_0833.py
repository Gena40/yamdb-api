# Generated by Django 2.2.16 on 2022-02-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220202_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(help_text='Дата добавления', verbose_name='Дата добавления'),
        ),
    ]