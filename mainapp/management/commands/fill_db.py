import json
import os
from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User


JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('mainapp_productcategory')
        # subcategories = load_from_json('mainapp_productsubcategory')

        ProductCategory.objects.all().delete()
        [ProductCategory.objects.create(**category) for category in categories]

        # ProductSubCategory.objects.all().delete()
        # [ProductSubCategory.objects.create(**subcategory) for subcategory in subcategories]

        products = load_from_json('mainapp_product')

        Product.objects.all().delete()
        for product in products:
            product['category'] = ProductCategory.objects.get(name=product['category'])
            # product['subcategory'] = ProductSubCategory.objects.get(name=product['subcategory'])
            new_product = Product(**product)
            new_product.save()

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', 'djangо@geekshop.local', 'geekbrains', age=25)

