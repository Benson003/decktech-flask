from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


    with open('app.key') as lock:
        app.secret_key = lock.read().strip()

    db.init_app(app)
    migrate.init_app(app,db)


    from app import routes
    routes.register_routes(app)
    
    with app.app_context():
        from app import models


    return app