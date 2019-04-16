from tinydb import TinyDB, Query
from flask_restful import Resource

databasePath = "SpendDB.json"

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
    }
]


class DatabaseConn(Resource):
    def __init__(self):
        self.__dbPath = databasePath
        self.__oConn = TinyDB(self.__dbPath)

    def create(self, data):
        return self.__oConn.insert(data)

    def read(self):
        return self.__oConn.all()

    def update(self, data):
        Spend = Query()
        return self.__oConn.update(data, Spend.id == data["id"])

    def delete(self, item_id):
        Spend = Query()
        return self.__oConn.remove(Spend.id == item_id)
