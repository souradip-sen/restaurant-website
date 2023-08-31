from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu, MenuCategory
from restaurant.serializers import MenuSerializer, MenuCategorySerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.url = reverse('menu')  # Replace 'menu-list' with your actual API endpoint URL name
        self.category = MenuCategory.objects.create(name="Test Category")
        self.client = APIClient()
        self.menus = [
            Menu.objects.create(title="Item 1", price=10.0, category=self.category, description="Description 1", inventory=50),
            Menu.objects.create(title="Item 2", price=20.0, category=self.category, description="Description 2", inventory=30),
        ]

    def test_getall(self):
        response = self.client.get(self.url)
        serializer = MenuSerializer(self.menus, many=True)
        response_data = response.data['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, serializer.data)
