from flask_restful import Resource
import logging as logger


class Root(Resource):
    def get(self):
        logger.debug("Class Root - Inside GET method")
        return {"message": "Class Root - Inside GET method"}, 200
