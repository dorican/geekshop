# Generated by Django 2.2.4 on 2019-08-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_product_to_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=128, unique=True, verbose_name='Слаг'),
        ),
    ]
