"""
Module init.
Contains function for starting up the flask process
"""
import logging

from api.routes import RouteManager
from api.server import WaitressAPIServer
from api.app import FlaskApp
from microlab.interface import MicrolabInterface


def run_flask(in_queue, out_queue):

    logging.info("### STARTING API ###")
    werkzeugLogger = logging.getLogger("werkzeug")
    # suppresses logging of individual requests to endpoints. Prevents log spam
    werkzeugLogger.setLevel(logging.WARNING)

    microlab_interface = MicrolabInterface(in_queue, out_queue)

    flask_app = FlaskApp()

    # This handles the routes and registering them to the flask_app instance
    RouteManager(flask_app, microlab_interface)

    server = WaitressAPIServer(flask_app.get_flask_app())
    server.set_microlab_interface(microlab_interface)
    server.run()
