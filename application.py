from bibliomart import app, create_app

application = app

with application.app_context():
    create_app()
