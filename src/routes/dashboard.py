from flask import Blueprint, jsonify, request
from src.utils import connect_to_mongodb, close_mongodb_connection
from bson.objectid import ObjectId

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/api/login', methods=['POST'])
def login():
    try:
        with connect_to_mongodb() as (client, db):
            users = db.users
            auth_key = request.headers.get('Authorization')
            user = users.find_one({'authKey': auth_key})

            if user:
                return jsonify({'message': 'Authentication successful'}), 200
            else:
                return jsonify({'error': 'Authentication failed'}), 401

    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
