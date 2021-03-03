import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from company.models import *


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
        self.data = {
            'name': 'Pharmacie Djerba 2',
            'license_number': 1234,
            'address': 'rue de la paix',
            'contact_number': 12345678,
            'email': 'email@email.com',
            'description': 'pharmacie de nuit tunis'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
