from django.test import TestCase
from restaurant.views import MenuItemView


class MenuItemViewTest(TestCase):

    def setUp(self):
        self.menu1 = MenuItemView.objects.create(
            name='Menu 1',
            price=100,
            items=[
                'Item 1',
                'Item 2',
                'Item 3',
            ]
        )
        self.menu2 = MenuItemView.objects.create(
            name='Menu 2',
            price=200,
            items=[
                'Item 4',
                'Item 5',
                'Item 6',
            ]
        )

    def test_getall(self):
        response = self.client.get('/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.menu1.name)
        self.assertEqual(response.data[0]['price'], self.menu1.price)
        self.assertEqual(response.data[0]['items'], self.menu1.items)
        self.assertEqual(response.data[1]['name'], self.menu2.name)
        self.assertEqual(response.data[1]['price'], self.menu2.price)
        self.assertEqual(response.data[1]['items'], self.menu2.items)
