# Generated by Django 2.2.3 on 2019-08-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190807_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, verbose_name='слаг'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, verbose_name='слаг'),
        ),
    ]
