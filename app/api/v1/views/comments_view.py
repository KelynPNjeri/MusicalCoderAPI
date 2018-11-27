"""Comments View"""
from flask_restplus import Api, Resource, reqparse
from ..models.comments_model import CommentsOps

class CommentList(Resource):
    """
    Handles all the Comments Endpoints.
    """
class Comment(Resource):
    """
    Handles 'GET' method for a single comment.
    """