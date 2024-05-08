from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('config.json', 'r') as f:
    config = json.load(f)

# Register blueprints
from src.routes.dashboard import dashboard_bp
from src.routes.offers import offers_bp
from src.routes.news import news_bp

app.register_blueprint(offers_bp)
app.register_blueprint(news_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(host=config['host'], port=config['port'], debug=config['debug'])
