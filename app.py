from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

myApp = Flask(__name__)

if __name__ == "__main__":
    logger.debug("Starting the application")
    from api import myApp

    myApp.run(debug=True)
