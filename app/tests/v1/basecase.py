"""Test Base Case"""
import unittest
from app import create_app

class BaseCase(unittest.TestCase):
    """
    BaseCase.
    """
    def setUp(self):
        """
        Setting Up Testing Environment
        """
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.content_type = "application/json"
        self.posts_payload = {
            "Post Title": "Beginning ES6 JavaScript.",
            "Post Body": "Lorem Ipsum.........",
            "Post Author": "Kelyn Paul",
            "Post Category": "JavaScript"
        }
        self.comments_payload = {
            "Comments Description": "Great Read, Keep up with the good work!",
            "Author": "Loren Travis"
        }
        self.registration_payload = {
            "Username": "Alan Turing",
            "Email": "alan.turing@gmail.com",
            "Password": "NewAccount@1234",
            "Confirm Password": "NewAccount@1234"
        }
        self.login_payload = {
            "Username": "Alan Turing",
            "Password": "NewAccount@1234"
        }

    def tearDown(self):
        """
        Destroying Test Environment.
        """
        self.app = None
        del self.posts_payload
        del self.comments_payload
        del self.registration_payload
        del self.login_payload
