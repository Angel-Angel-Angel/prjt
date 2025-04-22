from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from .models import User
        db.create_all()

        if User.query.count() == 0:

            from .sample_data import populate_sample_users
            populate_sample_users()

        from .routes import main
        app.register_blueprint(main)

    return app
