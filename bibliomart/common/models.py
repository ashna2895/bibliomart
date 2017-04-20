'''Defines models used in this app.'''

from datetime import datetime

import requests
from mongoengine.queryset import queryset_manager, QuerySet
from jsonschema import validate, ValidationError
