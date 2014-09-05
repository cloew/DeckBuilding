from routes import routes

from kao_flask.server import Server

server = Server(__name__, routes=routes)