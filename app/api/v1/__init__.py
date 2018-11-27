"""Creating Blueprints for the Version 1 of the API"""
from flask import Blueprint

# Local Imports
from .views.comments_view import CommentList, Comment
from .views.posts_view import PostList, Post
from .views.auth_view import UserRegistration, UserLogin

version1 = Blueprint('Version 1', __name__, url_prefix='/api/v1')
