from flask_restx import Namespace, Resource
from ..model.db import connect_to_db
from flask import jsonify, Response
from bson.objectid import ObjectId
from http import HTTPStatus
from bson import json_util


state_ns = Namespace('state', description='Namespace for State')

#   Serialize region data
def get_regions():
    database = connect_to_db()
    regions = database.regions

    data = list(regions.find())

    for item in data:
        item['_id'] = str(ObjectId(item['_id']))
    # database.close()
    return data

#   Serialize state data
def get_states(): 
    database = connect_to_db()
    states = database.data

    data = list(states.find())

    for item in data:
        item['_id'] = str(ObjectId(item['_id']))

    return data

#   Serialize lga data
def get_lgas():
    database = connect_to_db()
    lgas = database.local_governments

    data = list(lgas.find())

    # for item in data:
    #     item['_id'] = str(ObjectId(item['_id']))
    #     item['state_id'] = str(ObjectId(item['state_id']))

    return data


@state_ns.route('/regions')
class Regions(Resource):
    def get(self):
        """
            Get all regions
        """
        try:
            data = get_regions()

            response = jsonify(data)
            
            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR

@state_ns.route('/lgas')
class Lgas(Resource):
    def get(self):
        """
            Get all lgas
        """
        try:
            data = get_lgas()
            json_data = json_util.dumps(data)
            lgas = json_util.loads(json_data)

            for item in lgas:
                item['_id'] = str(ObjectId(item['_id']))
                item['state_id'] = str(ObjectId(item['state_id']))

            response = jsonify(lgas)

            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR

@state_ns.route('/states')
class States(Resource):
    def get(self):
        """
            Get all states
        """
        try:
            data = get_states()

            response = jsonify(data)

            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR