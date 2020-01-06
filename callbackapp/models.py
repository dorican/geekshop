from django.db import models


class CallbackApplication(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=128)
    phone = models.CharField(verbose_name='номер телефона', max_length=24)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.phone)

