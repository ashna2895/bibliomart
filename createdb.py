from bibliomart import app
from bibliomart.user.model import db
import datetime
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

#add sample entries
from bibliomart.user.model import Role
with app.app_context():
    roles = {
        'admin':"Administrator for the app",
        'buyer':'Users registered to buy books',
        'seller':'Users registered to sell books',
    }
    for role in roles:
        rol = Role(role,roles[role])
        db.session.add(rol)
    db.session.commit()
