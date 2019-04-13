from flask_restful import Api
from app import myApp

from .Root import Root
from .RootApi import RootApi

from .Spend import Spend
from .Devs import Devs

restServer = Api(myApp)

restServer.add_resource(Root, "/")
restServer.add_resource(RootApi, "/api")
restServer.add_resource(Spend, "/api/spend")
restServer.add_resource(Devs, "/api/devs")
