from flask import Flask
from flask.ext.cors import CORS
from flask.blueprints import Blueprint

import config
from model.abc import db
import route

server = Flask(__name__)
server.debug = config.DEBUG

server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(server)
db.app = server

CORS(
    server,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

for blueprint in vars(route).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT
        )

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
