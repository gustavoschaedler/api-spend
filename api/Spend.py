from flask_restful import Resource
import logging as logger


class Spend(Resource):

    def get(self):
        logger.debug("Class Spend - Inside GET method")
        return {"message": "Class Spend - Inside GET method"}, 200

    def post(self):
        logger.debug("Class Spend - Inside POST method")
        return {"message": "Class Spend - Inside POST method"}, 200

    def put(self):
        logger.debug("Class Spend - Inside PUT method")
        return {"message": "Class Spend - Inside PUT method"}, 200

    def delete(self):
        logger.debug("Class Spend - Inside DELETE method")
        return {"message": "Class Spend - Inside DELETE method"}, 200
