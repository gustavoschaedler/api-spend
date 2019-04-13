from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

if __name__ == "__main__":
    from api import flaskAppInstance

    logger.debug("Starting the application")

    flaskAppInstance.run(debug=True)
