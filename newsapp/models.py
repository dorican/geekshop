from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='заголовок новости', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='слаг новости', max_length=128, unique=True)
    image = models.ImageField(upload_to='product_images', default='users_avatars/default.jpg')
    content = models.TextField()
    author = models.CharField(verbose_name='автор новости', max_length=128)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
