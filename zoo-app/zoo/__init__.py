from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqldb://zooadmin:yUE3VTNwMEWnsAn@localhost/SpainZoo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from . import main

    app.register_blueprint(main.bp)
    return app
