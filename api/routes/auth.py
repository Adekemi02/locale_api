import uuid
import os
from dotenv import load_dotenv, find_dotenv
from flask_restx import Namespace, Resource, fields
from ..model.db import connect_to_db
from http import HTTPStatus
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from .views import cache
from functools import wraps
import jwt


load_dotenv(find_dotenv())

auth_ns = Namespace('auth', description='Namesake for Authentication')

#   User model
user_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='User first name'),
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

#   Login model
login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})


#   Generate API key model
generate_api_key_model = auth_ns.model('Generate API Key', {
    'project_name': fields.String(required=True, description='Project name'),
    'project_description': fields.String(description='Project description')
    
})

#   Database connection
database = connect_to_db()


#   API key required decorator
def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('API-Key')

        if api_key:
            user = database.users.find_one({'api_key': api_key})

            if user and user.is_active:
                return f(*args, **kwargs)
            
        return {'message': 'Invalid API key'}, HTTPStatus.UNAUTHORIZED
    
    return decorated_function

@auth_ns.route('/auth/register')
class SignUp(Resource):
    @auth_ns.expect(user_model)
    @auth_ns.doc(description='Register a new user')
    @cache.cached(timeout=60)
    def post(self):
        """
            Register a new user
        """

        data = request.get_json()

        #   Check if user already exists
        user = database.users.find_one({'email': data['email']})

        if user:
            return {'message': 'User already exists'}, HTTPStatus.BAD_REQUEST

        username = data['username']
        email = data['email']
        password = data['password']

        user = {
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password),
            'created_at': datetime.utcnow()
        }

        #   Insert user into database
        database.users.insert_one(user)

        return {'message': 'User created successfully'}, HTTPStatus.CREATED
    
@auth_ns.route('/auth/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.doc(description='Login a user', 
                 params={'email': 'User email address', 
                        'password': 'User password'})
    def post(self):
        """
            Login a user
        """

        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        #   Check if email and password are provided
        if not email or not password:
            return {'message': 'Email and password required'}, HTTPStatus.BAD_REQUEST
        
        #   Check if user exists
        user = database.users.find_one({'email': email})

        #   Check if user exists and password is correct
        if user and check_password_hash(user['password_hash'], password):

            api_key = user.get('api_key')

            if not api_key:

                #   Generate API key
                api_key = str(uuid.uuid4())

                #   Update user's api key
                database.users.update_one({'email': email}, {'$set': {'api_key': api_key}})

            #   Generate access and refresh tokens
            access_token = create_access_token(identity=str(ObjectId(user['_id'])))
            refresh_token = create_refresh_token(identity=str(ObjectId(user['_id'])))

            token_data = {
                'identity': str(ObjectId(user['_id'])),
                'api_key': api_key
            }

            #   Encode token data
            jwt_token = jwt.encode(token_data, 
                                   os.getenv('JWT_SECRET_KEY'),
                                    algorithm='HS256')

            response = {
                'message': 'User logged in',
                'api_key': api_key,
                'access_token': access_token,
                'refresh_token': refresh_token,
                'jwt_token': jwt_token
            }

            return response, HTTPStatus.OK

    
@auth_ns.route('/refresh')
class Refresh(Resource):
    @auth_ns.doc(description='Refresh a user\'s token')
    @cache.cached(timeout=60)
    @jwt_required(refresh=True)
    def post(self):
        """
            Refresh a user's token
        """

        current_user = get_jwt_identity()

        #   Generate new access token
        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}, HTTPStatus.OK

@auth_ns.route('/generate-api-key')
class GenerateApiKey(Resource):
    @auth_ns.expect(generate_api_key_model)
    @auth_ns.doc(description='Generate a new API key')
    @jwt_required()
    def post(self):
        """
            Generate a new API key
        """

        current_user = get_jwt_identity()

        data = request.get_json()

        project_name = data.get('project_name')
        project_description = data.get('project_description')

        #   Check if project name and description are provided
        if not project_name or not project_description:
            return {'message': 'Project name and description required'}, HTTPStatus.BAD_REQUEST
        
        generate_key_doc = {
            'project_name': project_name,
            'project_description': project_description,
            'api_key': database.users.find_one({'_id': ObjectId(current_user)})['api_key'],
            'created_at': datetime.utcnow()
        }

        #   Insert generate key document into database
        database.generate_keys.insert_one(generate_key_doc)

        #  Check if user has generated an API key for this project before
        if database.users.find_one({'_id': ObjectId(current_user), 'generate_keys.project_name': project_name}):
            return {'message': 'API key generated'}, HTTPStatus.OK
        

        return {'message': 'API key already generated'}, HTTPStatus.OK

    
@auth_ns.route('/logout')
class Logout(Resource):
    def post(self):
        """
            Logout a user
        """

        return {'message': 'User logged out'}
    
@auth_ns.route('/reset-password')
class ResetPassword(Resource):
    def post(self):
        """
            Reset a user's password
        """

        return {'message': 'Password reset'}
    
@auth_ns.route('/forgot-password')
class ForgotPassword(Resource):
    def post(self):
        """
            Forgot a user's password
        """

        return {'message': 'Password reset'}
    
@auth_ns.route('/confirm-email')
class ConfirmEmail(Resource):
    def post(self):
        """
            Confirm a user's email
        """

        return {'message': 'Email confirmed'}
    
@auth_ns.route('/resend-confirmation-email')
class ResendConfirmationEmail(Resource):
    def post(self):
        """
            Resend a user's confirmation email
        """

        return {'message': 'Email resent'}