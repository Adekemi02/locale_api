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

@state_ns.route('/states/<string:state_id>')
class State(Resource):
    def get(self, state_id):
        """
            Get a single state
        """
        try:
            database = connect_to_db()
            states = database.data

            state = states.find_one({'_id': ObjectId(state_id)})

            state['_id'] = str(ObjectId(state['_id']))

            response = jsonify(state)

            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
@state_ns.route('/lgas/<string:state_id>')
class Lga(Resource):
    def get(self, state_id):
        """
            Get all lgas in a state
        """
        try:
            database = connect_to_db()
            lgas = database.local_governments

            data = list(lgas.find({'state_id': ObjectId(state_id)}))

            for item in data:
                item['_id'] = str(ObjectId(item['_id']))
                item['state_id'] = str(ObjectId(item['state_id']))

            response = jsonify(data)

            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
@state_ns.route('/regions/<string:region_id>')
class Region(Resource):
    def get(self, region_id):
        """
            Get a single region
        """
        try:
            database = connect_to_db()
            regions = database.regions

            geo_political_zone = regions.find_one({'_id': ObjectId(region_id)})

            geo_political_zone['_id'] = str(ObjectId(geo_political_zone['_id']))

            response = jsonify(geo_political_zone)

            return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR
    
@state_ns.route('/search/<string:query>')
class Search(Resource):
    def get(self, query):
        """
            Search for a state or lga
        """
        try:
            database = connect_to_db()
            states = database.data
            lgas = database.local_governments
            regions = database.regions

            state = states.find_one({'state': query})
            lga = lgas.find_one({'lga': query})
            region = regions.find_one({'name': query})

            if state:
                state['_id'] = str(ObjectId(state['_id']))

                response = jsonify(state)

                return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
            
            elif lga:
                lga['_id'] = str(ObjectId(lga['_id']))
                lga['state_id'] = str(ObjectId(lga['state_id']))

                response = jsonify(lga)

                return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')

            elif region:
                region['_id'] = str(ObjectId(region['_id']))

                response = jsonify(region)

                return Response(response.get_data(), status=HTTPStatus.OK, mimetype='application/json')
                        
            else:
                return {'message': 'No results found'}, HTTPStatus.NOT_FOUND
        
        except Exception as e:
            print(e)

            return {'message': 'An error occurred'}, HTTPStatus.INTERNAL_SERVER_ERROR

@state_ns.route('/hello')
class Hello(Resource):
    def get(self):
        """
            Hello world
        """
        return {'message': 'Hello world'}, HTTPStatus.OK