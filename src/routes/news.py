from flask import Blueprint, jsonify, request
from src.utils import connect_to_mongodb, close_mongodb_connection, serialize_id
from bson.objectid import ObjectId

news_bp = Blueprint('news', __name__)


@news_bp.route('/api/news', methods=['GET'])
def get_news():
    try:
        client, db = connect_to_mongodb()
        news = db.news
        i = request.args.get('i')
        page = request.args.get('p')
        query = {}
        if i:
            query['limit'] = int(i)
        elif page:
            query['skip'] = int(page) * 9
            query['limit'] = 9
        else:
            query['limit'] = 9
        data = list(news.find({}, {'text': 0}).skip(query.get('skip', 0)).limit(query['limit']))
        close_mongodb_connection(client)
        data = serialize_id(data)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@news_bp.route('/api/news/<string:id>', methods=['GET'])
def get_news_one(id):
    try:
        client, db = connect_to_mongodb()
        news = db.news
        data = news.find_one({'_id': ObjectId(id)})
        close_mongodb_connection(client)
        data = serialize_id(data)
        if data:
            return jsonify(data), 200
        else:
            return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
