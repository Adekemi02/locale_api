from flask_restx import Namespace, Resource, fields


state_ns = Namespace('state', description='Namesake for State')


@state_ns.route('/states')
class States(Resource):
    def get(self):
        """
            Get all states
        """

        return {'message': 'Get all states'}