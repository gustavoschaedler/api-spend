from flask_restful import Api
from app import flaskAppInstance

from .Root import Root
from .RootApi import RootApi

from .Spend import Spend
from .Devs import Devs

restServer = Api(flaskAppInstance)

restServer.add_resource(Root, "/")
restServer.add_resource(RootApi, "/api")
restServer.add_resource(Spend, "/api/spend")
restServer.add_resource(Devs, "/api/devs")
