from flask import Flask
from flask_security import current_user, user_registered
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__, template_folder='common/templates', static_folder='common/static/')
app.config.from_pyfile('config.py')


db = SQLAlchemy()
mail = Mail(app)
mail.connect()

# Custom Jinja template search paths.
custom_template_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([
        'bibliomart/extensions/security/templates'
        # Add additional paths here
    ]),
])
app.jinja_loader = custom_template_loader


def create_app():
    db.init_app(app)

    from bibliomart.api import api
    from bibliomart.user.controller import usr
    from bibliomart.user.model import User
    from bibliomart.manager.controller import manager
    from bibliomart.homepage.controller import homepage
    from bibliomart.extensions.security.controller import security


    app.register_blueprint(homepage)
    app.register_blueprint(usr, url_prefix='/usr')
    app.register_blueprint(manager, url_prefix='/manager')

if __name__ == '__main__':
    create_app()
