# Generated by Django 2.2 on 2019-08-31 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_auto_20190831_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 11, 8, 51, 294341, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]