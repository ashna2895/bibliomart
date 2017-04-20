import requests

from flask import Flask, Blueprint, render_template, request, jsonify


from bibliomart.user.model import User, UserData


usr = Blueprint('usr', __name__, template_folder='templates')


@usr.route('/')
def get_index():
    return "Test"
 
