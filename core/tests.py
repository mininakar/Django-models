from django.test import TestCase, Client
from django.urls import reverse
from core import factories

# Create your tests here.
class MedicinesTest (TestCase):
    def setUp (self)->None:
        self.client = Client()
        self.med=factories.Medicines()

    def test_list (self):
        response = self.client.get(reverse ('core:med_list'))
        self.assertEqual (response.status_code, 200)
    def test_detail(self):
        response = self.client.get(reverse('core:med_list', kwargs={'pk': self.med.pk}))
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        data = {
            'name': 'test',
            'date_issue': '2020-05-05',
            'expiry_date': '2025-05-05',
            'price': '0'
        }
        response = self.client.post(path=reverse('core:med_update'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'test',
            'date_issue': '2020-05-05',
            'expiry_date': '2025-05-05',
            'price': '0'
        }
        response = self.client.post(path=reverse('core:med_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)