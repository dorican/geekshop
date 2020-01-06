# Generated by Django 2.2.3 on 2019-08-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='имя клиента')),
                ('phone', models.CharField(max_length=24, verbose_name='номер телефона')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='время')),
            ],
        ),
    ]
