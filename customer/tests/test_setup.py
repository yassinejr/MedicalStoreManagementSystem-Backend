import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from customer.models import *


class TestSetUp(APITestCase):
    def setUp(self):
        self.username = 'medicaluser'
        self.email = 'medicaluser@medical.com'
        self.user = User.objects.create_user(self.username, self.email)
        self.client.force_authenticate(user=self.user)
        self.company = Customer.objects.create(
            name='customer zarzis',
            phone=12345678,
            address='rue de la paix'
        )
        self.data = {
            'name': 'customer Djerba',
            'phone': 12342255,
            'address': 'rue de la paix'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
