import json

from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetUp


class CustomerTests(TestSetUp):
    def test_view_customers(self):
        url = reverse('customer:customer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_customer(self):
        url = reverse('customer:customer-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_detail(self):
        url = reverse('customer:customer-detail', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["name"], 'customer zarzis')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_update(self):
        url = reverse('customer:customer-detail', kwargs={"pk": 1})
        data = {
            'name':'customer djerba',
            'phone': 12342255,
            'address': 'rue de la paix'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['name'], 'customer djerba')
