from flask import Flask
from flask_cors import CORS
import json
from werkzeug.middleware.proxy_fix import ProxyFix
from src.routes.dashboard import dashboard_bp
from src.routes.offers import offers_bp
from src.routes.news import news_bp
from src.routes.form import form_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    configure_app(app)
    register_blueprints(app)
    return app


def configure_app(app):
    with open('config.json', 'r') as f:
        config = json.load(f)
        flask = config.get("FLASK", {})
        env = config.get("ENV", "dev")

    if env == "prod":
        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )
    app.config.update(flask)


def register_blueprints(app):
    app.register_blueprint(offers_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(form_bp)


if __name__ == "__main__":
    app = create_app()
    app.run()
