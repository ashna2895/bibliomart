import requests
from flask_restful import Api

from bibliomart import app

api = Api(app, prefix='/api')
