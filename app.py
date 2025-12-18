from flask import Flask
from database import db
from flasgger import Swagger
from presentation_layer.views.customer import customer_bp
from presentation_layer.views.driver import driver_bp
from presentation_layer.views.freight import freight_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///frete.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.config['SWAGGER'] = {
        'title': 'API de Fretes',
        'uiversion': 3,
        'tags': [
            {'name': 'Customers', 'description': 'Gestão de Clientes'},
            {'name': 'Drivers', 'description': 'Gestão de Motoristas'},
            {'name': 'Freights', 'description': 'Gestão de Fretes'}
        ]
    }

    Swagger(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(customer_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(freight_bp)

    return app


app = create_app()
