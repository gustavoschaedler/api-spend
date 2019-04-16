from flask_restful import Resource, abort
from flask import request
from db.db import DatabaseConn

import logging as logger

# db.insert(
#     {
#         "id": 4,
#         "desc": "compra de casacos",
#         "date": "02/01/2019",
#         "amount": 55.40,
#         "category": "Outros",
#         "whopaid": "Gustavo",
#         "percentual": 60,
#         "photoreceipt": "path/photos/casaco.jpg"
#     }
# )


def abort_if_spend_doesnt_exist(attribute, value, list_data):
    index = [item for item in list_data if item[attribute] == value]
    if len(index) == 0:
        abort(404, message="{}: '{}' doesn't exist".format(attribute, value))

# parser = reqparse.RequestParser()
# parser.add_argument('task')


class Spend(Resource):

    def __init__(self):
        self.__dbConn = DatabaseConn()

    def post(self):
        data = request.get_json()
        return self.__dbConn.create(data), 200

    def get(self):
        return self.__dbConn.read(), 200

    def put(self):
        data = request.get_json()
        return self.__dbConn.update(data), 200

    def delete(self):
        item_id = request.get_json()
        return self.__dbConn.delete(item_id["id"]), 200


class SpendById(Resource):

    def __init__(self):
        self.__dbConn = DatabaseConn()
        self.__spend_list = self.__dbConn.read()
        self.__attribute = "id"

    def get(self, spend_id):
        abort_if_spend_doesnt_exist(
            self.__attribute, spend_id, self.__spend_list)

        spend_by_id = [
            spend for spend in self.__spend_list if spend[self.__attribute] == spend_id]

        return spend_by_id, 200

    def put(self, spend_id):
        return {"message": "Class Spend - Inside PUT method"}, 200

    def delete(self, spend_id):
        return {"message": "Class Spend - Inside DELETE method"}, 200


class SpendByWhopaid(Resource):

    def __init__(self):
        self.__dbConn = DatabaseConn()
        self.__spend_list = self.__dbConn.read()
        self.__attribute = "whopaid"

    def get(self, spend_whopaid):
        logger.debug("Class SpendByWhopaid - Inside GET method")
        abort_if_spend_doesnt_exist(
            self.__attribute, spend_whopaid, self.__spend_list)

        spend_by_whopaid = [
            spend for spend in self.__spend_list if spend[self.__attribute] == spend_whopaid]

        return spend_by_whopaid, 200

    def put(self, spend_id):
        return {"message": "Class SpendByWhopaid - Inside PUT method"}, 200

    def delete(self, spend_id):
        return {"message": "Class SpendByWhopaid - Inside DELETE method"}, 200
