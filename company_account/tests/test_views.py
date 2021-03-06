import json

from django.urls import reverse
from rest_framework import status

from .test_setup import TestSetUp


class CompanyAccountTests(TestSetUp):
    def test_view_company_account(self):
        url = reverse('company_account:company-account-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_company_account(self):
        url = reverse('company_account:company-account-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_company_account_detail(self):
        url = reverse('company_account:company-account-detail', kwargs={"pk": 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data["company_id"], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_account_update(self):
        url = reverse('company_account:company-account-detail', kwargs={"pk": 1})
        data = {
            'company_id':1,
            'transaction_type': "Cash",
            'transaction_amount': 124236,
            'payment_mode': "Cash"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['company_id'], 1)
