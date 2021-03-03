from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from company.models import *
from company_account.models import *
from company_bank.models import *


class TestSetUp(APITestCase):
    def setUp(self):
        self.username = 'medicaluser'
        self.email = 'medicaluser@medical.com'
        self.user = User.objects.create_user(self.username, self.email)
        self.client.force_authenticate(user=self.user)
        self.company = Company.objects.create(
            name='Pharmacie Djerba',
            license_number=1234,
            address='rue de la paix',
            contact_number=12345678,
            email='email@email.com',
            description='pharmacie de nuit tunis'
        )
        self.company_account = CompanyAccount.objects.create(
            company_id=self.company,
            transaction_type = "Debit",
            transaction_amount = 12423,
            payment_mode = "Check",
        )
        self.data_account_to_update = {
            'company_id': 1,
            'transaction_type': "Debit",
            'transaction_amount': 12423,
            'payment_mode': "Check",
        }
        self.company_bank = CompanyBank.objects.create(
            company_id=self.company,
            bank_account_number=123456789123456,
            ifsc=12423,
        )
        self.data_bank_to_update = {
            'company_id': 1,
            'bank_account_number': 123456789123456,
            'ifsc': 12423,
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
