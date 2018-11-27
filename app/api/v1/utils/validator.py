"""This module handles all the input validation for the API."""
from flask_restplus import fields, Namespace


class PostsValidator:
    """
    Ensures correctness of the posts JSON input and the form of the output.
    """

    posts_namespace = Namespace(
        "Posts Endpoint",
        description="Deals with creating, editing and deleting of posts",
    )
    posts_model = posts_namespace.model(
        "Posts Model",
        {
            "Post Title": fields.String(description="Post Title"),
            "Post Body": fields.String(description="Post Body"),
            "Post Author": fields.String(description="Post Author"),
            "Post Category": fields.String(description="Post Category"),
        })
    post_response = posts_namespace.model(
        "API response for any GET request",
        {
            "Post ID": fields.Integer(description="UniquePost ID"),
            "Post Title": fields.String(description="Post Title"),
            "Post Body": fields.String(description="Post Body"),
            "Post Author": fields.String(description="Post Author"),
            "Post Category": fields.String(description="Post Category"),
            "Date Posted": fields.DateTime(dt_format="rfc822", description="Date Posted")
        })


class CommentsValidator:
    """
    Ensures correctness of the comments JSON input and the form of the output.
    """

    comments_namespace = Namespace(
        "Comments Endpoint",
        description="Deals with creating, editing and deleting of comments",
    )
    comments_model = comments_namespace.model("Comments Model", {
        "Comments Description": fields.String(description='Comment Body'),
        "Author": fields.String(description='Posted By')
    })
    comment_response = comments_namespace.model("Comment Endpoint Responese", {
        "Comments ID": fields.Integer(description="Auto Generated ID"),
        "Comments Description": fields.String(description="Comment Body"),
        "Author": fields.String(description="Comment Author"),
        "Date Posted": fields.DateTime(dt_format="rfc822", description="Date Posted")
    })

class UserValidator:
    """
    Ensures correctness of the comments JSON input and the form of the output.
    """
    user_namespace = Namespace('Auth Endpoint',
                               description="Deals with User Registration and Login.")
    user_registration_model = user_namespace.model("Register Endpoint", {
        "Username": fields.String(description="Username"),
        "Email": fields.String(description="User's email"),
        "Password": fields.String(description="Password"),
        "Confirm Password": fields.String(description="Password")
    })
    user_login_model = user_namespace.model("Login Endpoint", {
        "Username": fields.String(description="Username"),
        "Password": fields.String(description="Password")
    })
