from flask_restful import Resource
import logging as logger


class Devs(Resource):

    def get(self):
        logger.debug("Class Devs - Inside GET method")
        return {"message": "Class Devs - Inside GET method"}, 200

    def post(self):
        logger.debug("Class Devs - Inside POST method")
        return {"message": "Class Devs - Inside POST method"}, 200

    def put(self):
        logger.debug("Class Devs - Inside PUT method")
        return {"message": "Class Devs - Inside PUT method"}, 200

    def delete(self):
        logger.debug("Class Devs - Inside DELETE method")
        return {"message": "Class Devs - Inside DELETE method"}, 200
