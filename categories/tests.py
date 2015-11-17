import  json

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from .models import Category

# Create your tests here.
class CategoriesTest(TestCase):
    
    fixtures = [
        'users.json'
    ]
    
    def test_category_API(self):
            """ test category  API """
            url = reverse('api_categories_list')
            category = {
            "name": "books", 
            "description": "books to be shared",
        }
            
            # GET 200
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            
            # POST 403
            url = reverse('api_categories_create')
            response = self.client.post(url, json.dumps(category), content_type='application/json')
            self.assertEqual(403, response.status_code)
            print response.status_code
            self.client.login(username='stefano', password='stefano')
            response = self.client.post(url, json.dumps(category), content_type='application/json')
            self.assertEqual(403, response.status_code)
            
            # POST 201
            self.client.logout()
            self.client.login(username='admin', password='admin')
            response = self.client.post(url, json.dumps(category), content_type='application/json')
            self.assertEqual(201, response.status_code)
            
            
