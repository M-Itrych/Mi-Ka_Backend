from flask import Blueprint, jsonify
from src.utils import connect_to_mongodb, close_mongodb_connection, serialize_id
from bson.objectid import ObjectId

offers_bp = Blueprint('offers', __name__)


@offers_bp.route('/api/offers', methods=['GET'])
def get_offers():
    try:
        with connect_to_mongodb() as (client, db):
            offers = db.offers
            data = list(offers.find({}, {'contents': 0}))
            data = serialize_id(data)
            return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@offers_bp.route('/api/offers/<string:id>', methods=['GET'])
def get_offer(id):
    try:
        with connect_to_mongodb() as (client, db):
            offers = db.offers
            data = offers.find_one({'_id': ObjectId(id)})
            if data:
                return jsonify(data.get('contents')), 200
            else:
                return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
