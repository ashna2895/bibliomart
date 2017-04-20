from flask import Blueprint, render_template, jsonify, make_response, request
from flask_restful import Resource, reqparse, inputs
from flask_security import current_user, login_required, roles_accepted

manager = Blueprint('manager', __name__, template_folder='templates',
    static_folder='static')

@manager.route('/users')
@login_required
@roles_accepted('admin','manager')
def manager_users():
    return render_template('users.html', page='manager')
