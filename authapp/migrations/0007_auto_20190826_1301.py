# Generated by Django 2.2.4 on 2019-08-26 10:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190826_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 28, 10, 1, 27, 391115, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
