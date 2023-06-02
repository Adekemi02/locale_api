from flask_restx import Namespace, Resource, fields


auth_ns = Namespace('auth', description='Namesake for Authentication')

user_model = auth_ns.model('User', {
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

@auth_ns.route('/register')
class SignUp(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """
            Register a new user
        """

        return {'message': 'User registered'}
    
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        """
            Login a user
        """

        return {'message': 'User logged in'}
    
@auth_ns.route('/refresh')
class Refresh(Resource):
    def post(self):
        """
            Refresh a user's token
        """

        return {'message': 'Token refreshed'}
    
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