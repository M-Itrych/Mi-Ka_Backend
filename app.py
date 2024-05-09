from flask import Flask
from flask_cors import CORS
import json
from src.routes.dashboard import dashboard_bp
from src.routes.offers import offers_bp
from src.routes.news import news_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    configure_app(app)
    register_blueprints(app)
    return app


def configure_app(app):
    with open('config.json', 'r') as f:
        config = json.load(f)
    app.config.update(config)


def register_blueprints(app):
    app.register_blueprint(offers_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(dashboard_bp)


if __name__ == "__main__":
    app = create_app()
    app.run()