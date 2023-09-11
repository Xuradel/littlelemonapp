from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from reservations.models import MenuTable  # Import the Menu model
from reservations.serializers import MenuTableSerializer  # Import the serializer for Menu


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create test instances of the Menu model
        MenuTable.objects.create(name="Item 1", price=10.99)
        MenuTable.objects.create(name="Item 2", price=15.99)
        MenuTable.objects.create(name="Item 3", price=8.49)
    
    def test_getall(self):
            # Define the URL to retrieve all Menu objects
            # Assuming 'menu-list' is the URL pattern for your Menu view
        url = reverse('menu/items/')

        # Perform a GET request to retrieve all Menu objects
        response = self.client.get(url)

        # Serialize the Menu objects from the database
        menus = MenuTable.objects.all()
        serializer = MenuTableSerializer(menus, many=True)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data in the response matches the expected serialized data
        self.assertEqual(response.data, serializer.data)