from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.offers import offers_bp
from routes.news import news_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(offers_bp)
app.register_blueprint(news_bp)

if __name__ == "__main__":
    app.run()
