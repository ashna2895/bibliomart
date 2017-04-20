from flask_security import (Security, SQLAlchemyUserDatastore,
    UserMixin, RoleMixin)
from flask_security.forms import RegisterForm
from wtforms import StringField, validators

from bibliomart import app, db
from bibliomart.user.model import User, Role, UserData


class ExtendedRegisterForm(RegisterForm):
    name = StringField('Name', [validators.Required()])
    mobile = StringField('Mobile', [validators.Required()])

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

@security.context_processor
def security_context_processor():
    return dict(page="security")
