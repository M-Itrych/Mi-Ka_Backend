from flask import Flask
from flask_cors import CORS

from src.routes.dashboard import dashboard_bp
from src.routes.offers import offers_bp
from src.routes.news import news_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(offers_bp)
app.register_blueprint(news_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run()
