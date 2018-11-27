import unittest
from app import create_app

class BaseCase(unittest.TestCase):
    """
    BaseCase.
    """
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
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
            
        }

    def tearDown(self):
        pass