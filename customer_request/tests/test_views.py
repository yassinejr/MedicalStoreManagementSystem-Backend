import json

from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetUp


class CustomerRequestTests(TestSetUp):
    def test_view_customer_request(self):
        url = reverse('customer_request:customer-request-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_customer_request(self):
        url = reverse('customer_request:customer-request-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_request_detail(self):
        url = reverse('customer_request:customer-request-detail', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["customer_name"], 'customer zarzis')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_request_update(self):
        url = reverse('customer_request:customer-request-detail', kwargs={"pk": 1})
        data = {
            'customer_name': 'customer djerba',
            'phone': 12342255,
            'medicine_detail': 'Aspegic',
            'status': True,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['customer_name'], 'customer djerba')
