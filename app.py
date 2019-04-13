from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

myApp = Flask(__name__)

if __name__ == "__main__":
    from api import myApp

    logger.debug("Starting the application")

    myApp.run(debug=True)
