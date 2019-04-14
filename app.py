from flask import Flask
from flask_restful import Api
import logging as logger

from api.Root import Root
from api.RootApi import RootApi
from api.Spend import Spend, SpendById, SpendByWhopaid
from api.Devs import Devs

logger.basicConfig(level="DEBUG")

myApp = Flask(__name__)

restServer = Api(myApp)

restServer.add_resource(Root, "/")
restServer.add_resource(RootApi, "/api")

restServer.add_resource(Spend, "/api/spend")
restServer.add_resource(SpendById, "/api/spend/id/<int:spend_id>")
restServer.add_resource(
    SpendByWhopaid, "/api/spend/whopaid/<string:spend_whopaid>")

restServer.add_resource(Devs, "/api/devs")

if __name__ == "__main__":
    logger.debug("Starting the application")

    myApp.run(debug=True)
