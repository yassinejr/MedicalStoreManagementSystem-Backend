import json

from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetUp


class CompanyTests(TestSetUp):
    def test_view_companies(self):
        url = reverse('company:company-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company(self):
        url = reverse('company:company-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_company_detail(self):
        url = reverse('company:company-detail', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["name"], 'Pharmacie Djerba')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_update(self):
        url = reverse('company:company-detail', kwargs={"pk": 1})
        data = {
            'name': 'Pharmacie Zarzis',
            'license_number': 1234,
            'address': 'rue de la paix',
            'contact_number': 11223344,
            'email': 'email@email.com',
            'description': 'pharmacie de nuit zarzis'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['name'], 'Pharmacie Zarzis')
