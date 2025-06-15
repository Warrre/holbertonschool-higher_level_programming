#!/usr/bin/env python

"""Test cases for Task 5: Basic Security"""



import unittest

import json

from task_05_basic_security import app





class TestBasicSecurity(unittest.TestCase):

    """Test class for basic security implementation"""



    def setUp(self):

        """Set up test client"""

        self.app = app.test_client()

        self.app.testing = True



    def test_basic_auth_no_credentials(self):

        """Test basic auth route without credentials"""

        response = self.app.get('/basic-protected')

        self.assertEqual(response.status_code, 401)



    def test_basic_auth_valid_credentials(self):

        """Test basic auth route with valid credentials"""

        credentials = ('user1', 'password')

        response = self.app.get('/basic-protected', 

                              auth=credentials)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data.decode(), 'Basic Auth: Access Granted')



    def test_basic_auth_invalid_credentials(self):

        """Test basic auth route with invalid credentials"""

        credentials = ('user1', 'wrongpassword')

        response = self.app.get('/basic-protected',

                              auth=credentials)

        self.assertEqual(response.status_code, 401)



    def test_login_valid_credentials(self):

        """Test login route with valid credentials"""

        data = {

            'username': 'user1',

            'password': 'password'

        }

        response = self.app.post('/login',

                               json=data,

                               content_type='application/json')

        self.assertEqual(response.status_code, 200)

        self.assertTrue('access_token' in json.loads(response.data))



    def test_login_invalid_credentials(self):

        """Test login route with invalid credentials"""

        data = {

            'username': 'user1',

            'password': 'wrongpassword'

        }

        response = self.app.post('/login',

                               json=data,

                               content_type='application/json')

        self.assertEqual(response.status_code, 401)



    def test_jwt_protected_no_token(self):

        """Test JWT protected route without token"""

        response = self.app.get('/jwt-protected')

        self.assertEqual(response.status_code, 401)



    def test_jwt_protected_with_token(self):

        """Test JWT protected route with valid token"""

        # First login to get token

        login_data = {

            'username': 'user1',

            'password': 'password'

        }

        login_response = self.app.post('/login',

                                     json=login_data,

                                     content_type='application/json')

        token = json.loads(login_response.data)['access_token']

        

        # Test protected endpoint with token

        headers = {'Authorization': f'Bearer {token}'}

        response = self.app.get('/jwt-protected', headers=headers)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data.decode(), 'JWT Auth: Access Granted')



    def test_admin_only_with_user_token(self):

        """Test admin-only route with user token"""

        # Login as regular user

        login_data = {

            'username': 'user1',

            'password': 'password'

        }

        login_response = self.app.post('/login',

                                     json=login_data,

                                     content_type='application/json')

        token = json.loads(login_response.data)['access_token']

        

        # Test admin endpoint with user token

        headers = {'Authorization': f'Bearer {token}'}

        response = self.app.get('/admin-only', headers=headers)

        self.assertEqual(response.status_code, 403)



    def test_admin_only_with_admin_token(self):

        """Test admin-only route with admin token"""

        # Login as admin

        login_data = {

            'username': 'admin1',

            'password': 'password'

        }

        login_response = self.app.post('/login',

                                     json=login_data,

                                     content_type='application/json')

        token = json.loads(login_response.data)['access_token']

        

        # Test admin endpoint with admin token

        headers = {'Authorization': f'Bearer {token}'}

        response = self.app.get('/admin-only', headers=headers)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data.decode(), 'Admin Access: Granted')





if __name__ == '__main__':

    unittest.main()
