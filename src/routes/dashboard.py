from flask import Blueprint, jsonify, request
from src.utils import connect_to_mongodb, close_mongodb_connection, get_date_string, validate_news

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/api/authenticate', methods=['POST'])
def authenticate():
    try:
        auth_key = request.authorization
        if not auth_key:
            return jsonify({'error': 'Authentication credentials not provided'}), 401

        client, db = connect_to_mongodb()
        users = db.users
        auth_user = users.find_one({'authKey': str(auth_key)})
        close_mongodb_connection(client)

        if auth_user:
            return jsonify({'message': 'Private access granted'}), 200
        else:
            return jsonify({'error': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500


@dashboard_bp.route('/api/add/news', methods=['POST'])
def add_news():
    try:
        auth_key = request.authorization
        if not auth_key:
            return jsonify({'error': 'Authentication credentials not provided'}), 401

        client, db = connect_to_mongodb()
        users = db.users
        auth_user = users.find_one({'authKey': str(auth_key), 'role': {'$in': ['superadmin', 'admin']}})
        if auth_user:
            news_payload = {
                'date': get_date_string(),
                'title': request.json.get('title', ''),
                'desc': request.json.get('description', ''),
                'img': {
                    'url': request.json.get('url', ''),
                    'alt': request.json.get('alt', '')
                },
                'text': request.json.get('text', '')
            }

            is_valid, error_message = validate_news(data=news_payload)
            if not is_valid:
                return jsonify({'error': error_message}), 400

            db.news.insert_one(news_payload)
            return jsonify({'message': 'News added successfully'}), 200
        else:
            return jsonify({'error': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
