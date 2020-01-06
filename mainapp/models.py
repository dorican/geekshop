from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


# class ProductSubCategory(models.Model):
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     name = models.CharField(verbose_name='Имя подкатегории', max_length=128, unique=True)
#     description = models.TextField(verbose_name='Описание подкатегории', blank=True)
#
#     def __str__(self):
#         return f"{self.name}"
#
#     class Meta:
#         verbose_name = 'Подкатегория товара'
#         verbose_name_plural = 'Подкатегории товаров'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE, default=None)
    name = models.CharField(verbose_name='Название товара', max_length=128, unique=True)
    slug = models.SlugField(verbose_name='слаг', max_length=128, unique=True)
    image = models.ImageField(upload_to='product_images', default='users_avatars/default.jpg')
    short_desc = models.TextField(verbose_name='Краткое описание товара', blank=True)
    description = models.TextField(verbose_name='Полное описание товара', blank=True)
    price = models.DecimalField(verbose_name='Цена товара', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='На складе', default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)
    to_order = models.BooleanField(verbose_name='Под заказ', default=False)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
