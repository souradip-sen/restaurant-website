from django.test import TestCase
from restaurant.models import Menu, MenuCategory

class MenuTest(TestCase):
    def test_get_item(self):
        category = MenuCategory.objects.create(name="Desserts")
        item = Menu.objects.create(title="IceCream", price=80, inventory=100, category=category, description="Icecream")
        self.assertEqual(str(item), "IceCream : 80")