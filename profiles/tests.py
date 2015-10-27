import  json

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from .models import Profile as User

# Create your tests here.
class ProfilesTest(TestCase):
    
    def test_profile_API(self):
            """ test new user creation through the API """
            url = reverse('profile-list')
            # GET 200
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            
            
            new_user = {
            "poi": 'POINT(12 12)',
            "username": "stefano",
            "email": "stefano@gmail.com",
            "password": "test",
            "confirm_password": "test"
                }
            response = self.client.post(url, json.dumps(new_user), content_type='application/json')
            self.assertEqual(201, response.status_code)
