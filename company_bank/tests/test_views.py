import json

from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetUp


class CompanyBankTests(TestSetUp):
    def test_view_company_bank(self):
        url = reverse('company_bank:company-bank-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company_bank(self):
        url = reverse('company_bank:company-bank-list')
        response = self.client.post(url, self.data_bank_to_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_company_bank_detail(self):
        url = reverse('company_bank:company-bank-detail', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["company_id"], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_bank_update(self):
        url = reverse('company_bank:company-bank-detail', kwargs={"pk": 1})
        data = {
            'company_id': 1,
            'bank_account_number': 11223366554477,
            'ifsc': 12423,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['company_id'], 1)
