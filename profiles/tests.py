import  json

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from .models import Profile as User

# Create your tests here.
class ProfilesTest(TestCase):
    
    def test_profile_API(self):
            """ test new profile creation through the API """
            url = reverse('api_profile_list_create')
            
            # GET 200
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            
            # POST 201
            user1 = {
            "poi": 'POINT(12 12)',
            "username": "stefano",
            "email": "stefano@gmail.com",
            "password": "test",
            "confirm_password": "test"
                }
            user2 = {
            "poi": 'POINT(55 55)',
            "username": "pippo",
            "email": "stefano@gmail.com",
            "password": "test",
            "confirm_password": "test"
                }
            response = self.client.post(url, json.dumps(user1), content_type='application/json')
            self.assertEqual(201, response.status_code)
            response = self.client.post(url, json.dumps(user2), content_type='application/json')
            self.assertEqual(201, response.status_code)
            ## PROFILE UPDATE
            
            update_user = {
            "poi": 'POINT(15 12)',
            "email": "stefano@gmail.com",
                }
            url = reverse('api_profile_details',args=['1'])
            
            # PUT: 403 - unauthenticated
            response = self.client.post(url, json.dumps(update_user), content_type='application/json')
            self.assertEqual(403, response.status_code)
            
            ## PUT: 200 - authenticated
            self.client.login(username='stefano', password='test')
            response = self.client.put(url, json.dumps(update_user), content_type='application/json')
            self.assertEqual(200, response.status_code)
            
            # Put: 403 - not profile's owner
            self.client.logout()            
            self.client.login(username='pippo', password='test')
            response = self.client.put(url, json.dumps(update_user), content_type='application/json')
            self.assertEqual(403, response.status_code)
            
            #Put: 200 - profile's owner
            url = reverse('api_profile_details',args=['2'])
            response = self.client.put(url, json.dumps(update_user), content_type='application/json')
            self.assertEqual(200, response.status_code)
