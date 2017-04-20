from flask import Blueprint, render_template, request
from flask_security import current_user
import requests

from flask_restful import reqparse


homepage = Blueprint('homepage', __name__, template_folder='templates',
	static_folder='static/build', static_url_path='/homepage')


@homepage.route('/')
def index():
	return render_template('index.html',page='homepage')
