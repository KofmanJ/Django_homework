from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Фрукты', 'category_description': 'Свежие'},
            {'category_name': 'Овощи', 'category_description': 'Свежие'},
            {'category_name': 'Мясо', 'category_description': 'Замороженное'},
            {'category_name': 'Овощи', 'category_description': 'Замороженные'},
            {'category_name': 'Мясо', 'category_description': 'Свежее'},
        ]

        # for product in category_list:
        #     Category.objects.create(**product)

        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)
