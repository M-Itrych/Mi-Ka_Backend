from bson import ObjectId
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

        if not auth_user:
            close_mongodb_connection(client)
            return jsonify({'error': 'Authentication failed'}), 401

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
        close_mongodb_connection(client)
        return jsonify({'message': 'News added successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500


@dashboard_bp.route('/api/delete/news', methods=['POST'])
def delete_news():
    try:
        auth_key = request.authorization
        if not auth_key:
            return jsonify({'error': 'Authentication credentials not provided'}), 401

        client, db = connect_to_mongodb()
        users = db.users
        auth_user = users.find_one({'authKey': str(auth_key), 'role': 'superadmin'})
        if not auth_user:
            close_mongodb_connection(client)
            return jsonify({'error': 'Authentication failed'}), 401

        id = request.json.get('id', '')
        db.news.delete_one({'_id': ObjectId(id)})
        return jsonify({'message': 'News deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500


@dashboard_bp.route('/api/update/news', methods=['POST'])
def update_news():
    try:
        auth_key = request.authorization
        if not auth_key:
            return jsonify({'error': 'Authentication credentials not provided'}), 401

        client, db = connect_to_mongodb()
        users = db.users
        auth_user = users.find_one({'authKey': str(auth_key), 'role': {'$in': ['superadmin', 'admin']}})
        if not auth_user:
            close_mongodb_connection(client)
            return jsonify({'error': 'Authentication failed'}), 401

        news_id = request.json.get('id')
        if not news_id:
            close_mongodb_connection(client)
            return jsonify({'error': 'News ID not provided'}), 400

        existing_news = db.news.find_one({'_id': ObjectId(news_id)})
        if not existing_news:
            close_mongodb_connection(client)
            return jsonify({'error': 'News article not found'}), 404

        update_fields = {}
        if 'title' in request.json and request.json['title']:
            update_fields['title'] = request.json['title']
        if 'description' in request.json and request.json['description']:
            update_fields['description'] = request.json['description']
        if 'url' in request.json and request.json['url']:
            update_fields['img.url'] = request.json['url']
        if 'alt' in request.json and request.json['alt']:
            update_fields['img.alt'] = request.json['alt']
        if 'text' in request.json and request.json['text']:
            update_fields['text'] = request.json['text']

        db.news.update_one({'_id': ObjectId(news_id)}, {'$set': update_fields})

        close_mongodb_connection(client)
        return jsonify({'message': 'News article updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
