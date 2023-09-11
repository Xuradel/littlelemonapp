from django.test import TestCase
from reservations.models import MenuTable
#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")