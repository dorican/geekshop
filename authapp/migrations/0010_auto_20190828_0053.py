# Generated by Django 2.2.4 on 2019-08-27 21:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20190828_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='language',
            field=models.CharField(blank=True, max_length=38, verbose_name='язык'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 29, 21, 53, 40, 305875, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='country',
            field=models.CharField(blank=True, max_length=38, verbose_name='страна'),
        ),
    ]
