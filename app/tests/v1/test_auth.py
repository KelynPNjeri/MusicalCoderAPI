"""Testing the Auth Endpoint."""
import json
from .basecase import BaseCase as bc

class TestAuth(bc):
    """
    Testing the Registration and Login endpoints.
    """
    def setUp(self):
        bc.setUp(self)
    def test_user_registration(self):
        """
        Testing User Registration.
        """
        response = self.client.post('/api/v1/register', 
                                    data=json.dumps(self.registration_payload),
                                    content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn(data["message"], "User registered successfully. Please Login.")
    
    def test_user_login(self):
        """
        Testing User Login.
        """
        response = self.client.post('/api/v1/register', 
                                    data=json.dumps(self.registration_payload),
                                    content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn(data["message"], "User registered successfully. Please Login.")
        login_response = self.client.post('/api/v1/login', 
                                          data=json.dumps(self.login_payload), 
                                          content_type=self.content_type)
        login_data = json.loads(login_response.data.decode())
        self.assertEqual(login_response.status_code, 200)
        self.assertIn(login_data["message"], "Login Successful.")

    def tearDown(self):
        bc.tearDown(self)
