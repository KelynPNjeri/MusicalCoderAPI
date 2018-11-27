"""Testing the Posts Endpoint."""
import json
from .basecase import BaseCase as bc

class TestPosts(bc):
    """
    Testing Posts Endpoints
    """
    def setUp(self):
        bc.setUp(self)

    def test_creating_posts(self):
        """
        Testing Creating a new product.
        """
        response = self.client.post('/api/v1/posts',
                                    data=json.dumps(self.posts_payload),
                                    content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn(data["message"], "Post Created Successfully.")

    def test_fetching_all_posts(self):
        """
        Testing fetching all the posts.
        """
        response = self.client.post('/api/v1/posts',
                                    data=json.dumps(self.posts_payload),
                                    content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Post Created Successfully.")
        get_response = self.client.get('/api/v1/posts', content_type=self.content_type)
        get_data = json.loads(get_response.data.decode())
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_data["message"], "Success")


    def test_fetching_single_post(self):
        """
        Testing fetching a single post.
        """
        response = self.client.post('/api/v1/posts',
                                    data=json.dumps(self.posts_payload),
                                    content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["message"], "Post Created Successfully.")
        get_response = self.client.get('/api/v1/posts/1', content_type=self.content_type)
        get_data = json.loads(get_response.data.decode())
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_data["message"], "Success")

    def test_editing_posts(self):
        """
        Test Editing a Post.
        """
        post_response = self.client.post('/api/v1/posts',
                                         data=json.dumps(self.posts_payload),
                                         content_type=self.content_type)
        post_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_data["message"], "Post Created Successfully.")
        response = self.client.put('/api/v1/posts/{}'.format(post_data['post']['Post ID']), 
                                   data={
                                       "Post Title": "Beginning React.",
                                       "Post Body": "Lorem Ipsum.........",
                                       "Post Author": "Kelyn Paul",
                                       "Post Category": "JavaScript"
                                    }, content_type=self.content_type)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['post'][0]["Post Title"], "Beginning React")
    def test_deleting_posts(self):
        """
        Test Deleting a Post.
        """
        post_response = self.client.post('/api/v1/posts',
                                         data=json.dumps(self.posts_payload),
                                         content_type=self.content_type)
        post_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_data["message"], "Post Created Successfully.")
        response = self.client.delete('/api/v1/posts/{}'.format(post_data['post']['Post ID']))
        self.assertEqual(response.status_code, 200)

        # Confirming Delete.
        deleted_item_response = self.client.get('/api/v1/posts/{}'.format(post_data['post']['Post ID']))
        data = json.loads(deleted_item_response.data.decode())
        self.assertEqual(deleted_item_response.status_code, 404)
        self.assertEqual(data['message'], "Post Not Found")
        
    def tearDown(self):
        bc.tearDown(self)   
