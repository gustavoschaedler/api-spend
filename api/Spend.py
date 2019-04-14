from flask_restful import Resource, abort
from flask import jsonify

import logging as logger

SPEND = [
    {
        "id": 1,
        "desc": "compras da semana no mercado",
        "date": "25/03/2019",
        "amount": 12.34,
        "category": "Mercado",
        "whopaid": "Gustavo",
        "percentual": 60,
        "photoreceipt": "path/photos/arq.jpg"
    },
    {
        "id": 2,
        "desc": "viagem para franca",
        "date": "20/03/2019",
        "amount": 150.34,
        "category": "Viagem",
        "whopaid": "Gustavo",
        "percentual": 60,
        "photoreceipt": "path/photos/viagem.jpg"
    },
    {
        "id": 3,
        "desc": "compras para fazer sushi",
        "date": "03/04/2019",
        "amount": 25.32,
        "category": "Mercado",
        "whopaid": "Gustavo",
        "percentual": 60,
        "photoreceipt": "path/photos/mercado2.jpg"
    },
    {
        "id": 4,
        "desc": "compra de casacos",
        "date": "02/01/2019",
        "amount": 55.40,
        "category": "Outros",
        "whopaid": "Gustavo",
        "percentual": 60,
        "photoreceipt": "path/photos/casaco.jpg"
    },
    {
        "id": 5,
        "desc": "compras no mercado para semana",
        "date": "21/03/2019",
        "amount": 12.34,
        "category": "Mercado",
        "whopaid": "Gustavo",
        "percentual": 60,
        "photoreceipt": "path/photos/tesco.jpg"
    }
]


def abort_if_spend_doesnt_exist(attribute, value, list_data):
    index = [spend for spend in list_data if spend[attribute] == value]
    if len(index) == 0:
        abort(404, message="{}: {} doesn't exist".format(attribute, value))

# parser = reqparse.RequestParser()
# parser.add_argument('task')


class Spend(Resource):

    def __init__(self):
        self.__spend_list = SPEND

    def get(self):
        logger.debug("Class Spend - Inside GET method")
        #abort_if_spend_doesnt_exist(self.__attribute, spend_id, self.__spend_list)

        return self.__spend_list, 200

    def post(self):
        logger.debug("Class Spend - Inside POST method")
        return {"message": "Class Spend - Inside POST method"}, 200

    def put(self):
        logger.debug("Class Spend - Inside PUT method")
        return {"message": "Class Spend - Inside PUT method"}, 200

    def delete(self):
        logger.debug("Class Spend - Inside DELETE method")
        return {"message": "Class Spend - Inside DELETE method"}, 200


class SpendById(Resource):

    def __init__(self):
        self.__spend_list = SPEND
        self.__attribute = "id"

    def get(self, spend_id):
        logger.debug("Class Spend - Inside GET method")
        abort_if_spend_doesnt_exist(
            self.__attribute, spend_id, self.__spend_list)

        spend_by_id = [
            spend for spend in self.__spend_list if spend[self.__attribute] == spend_id]

        return spend_by_id, 200

    # def post(self, spend_id):
    #    logger.debug("Class Spend - Inside POST method")
    #    return {"message": "Class Spend - Inside POST method"}, 200

    def put(self, spend_id):
        logger.debug("Class Spend - Inside PUT method")
        return {"message": "Class Spend - Inside PUT method"}, 200

    def delete(self, spend_id):
        logger.debug("Class Spend - Inside DELETE method")
        return {"message": "Class Spend - Inside DELETE method"}, 200


class SpendByWhopaid(Resource):

    def __init__(self):
        self.__spend_list = SPEND
        self.__attribute = "whopaid"

    def get(self, spend_whopaid):
        logger.debug("Class SpendByWhopaid - Inside GET method")
        abort_if_spend_doesnt_exist(
            self.__attribute, spend_whopaid, self.__spend_list)

        spend_by_whopaid = [
            spend for spend in self.__spend_list if spend[self.__attribute] == spend_whopaid]

        return spend_by_whopaid, 200

    def put(self, spend_id):
        logger.debug("Class SpendByWhopaid - Inside PUT method")
        return {"message": "Class SpendByWhopaid - Inside PUT method"}, 200

    def delete(self, spend_id):
        logger.debug("Class SpendByWhopaid - Inside DELETE method")
        return {"message": "Class SpendByWhopaid - Inside DELETE method"}, 200
