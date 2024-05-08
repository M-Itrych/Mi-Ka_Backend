from flask import Blueprint, jsonify, request
from src.utils import connect_to_mongodb, serialize_id
from bson.objectid import ObjectId

news_bp = Blueprint('news', __name__)


@news_bp.route('/api/news', methods=['GET'])
def get_news():
    try:
        with connect_to_mongodb() as (client, db):
            news = db.news

            limit = int(request.args.get('i', 9))
            page = int(request.args.get('p', 0))
            skip = page * limit

            # Fetch data based on query parameters
            data = list(news.find().skip(skip).limit(limit))
            data = serialize_id(data)
            return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': f"Error fetching news: {str(e)}"}), 500


@news_bp.route('/api/news/<string:id>', methods=['GET'])
def get_news_one(id):
    try:
        with connect_to_mongodb() as (client, db):
            news = db.news
            data = news.find_one({'_id': ObjectId(id)})
            if data:
                return jsonify(data.get('content')), 200
            else:
                return jsonify({'error': 'News not found'}), 404
    except Exception as e:
        return jsonify({'error': f"Error fetching news: {str(e)}"}), 500
