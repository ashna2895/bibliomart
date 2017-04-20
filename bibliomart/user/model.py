import datetime
import uuid

from bson.objectid import ObjectId
from flask_security import UserMixin, RoleMixin

from bibliomart import db

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    def __init__(self, role, description):
        self.name = role
        self.description = description

class User(db.Model, UserMixin):
    """The base class model for Users"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)

    authenticated = db.Column(db.Boolean, default=False)
    verified = db.Column(db.Boolean, default = False)
    active = db.Column(db.Boolean())


    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)


    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class UserData(db.Model):
    """docstring forUserData."""
    __tablename__ = "user_data"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    alt_phone = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)

    def __init__(self, user_id, mobile, alt_phone, address, city, state, country, user_role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.alt_phone = alt_phone
        self.pwdhash = generate_password_hash(password)
        self.created_on = datetime.datetime.utcnow()
        self.updated_on = datetime.datetime.utcnow()
        self.user_role = user_role
        self.address = address
        self.city = city
        self.state = state
        self.country = country
