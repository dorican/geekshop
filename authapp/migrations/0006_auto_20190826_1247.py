# Generated by Django 2.2.4 on 2019-08-26 09:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20190825_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 28, 9, 47, 18, 739005, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]