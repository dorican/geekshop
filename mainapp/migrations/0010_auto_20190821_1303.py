# Generated by Django 2.2.3 on 2019-08-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20190816_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, verbose_name='слаг'),
        ),
    ]
