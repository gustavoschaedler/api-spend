from flask_restful import Resource
import logging as logger


class RootApi(Resource):
    def get(self):
        logger.debug("Class RootApi - Inside GET method")
        return {"message": "Class RootApi - Inside GET method"}, 200
