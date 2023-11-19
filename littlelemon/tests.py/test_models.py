from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):

    @classmethod
    def test_get_item(self):
        item = MenuItem.objects.create(
            title='IceCream', price=80, inventory=100)
        self.assertEqual(item, 'IceCream : 80')

    def test_fields(self):
        self.assertIsInstance(self.MenuItem.title, str)

        self.assertIsInstance(self.MenuItem.inventory, int)
