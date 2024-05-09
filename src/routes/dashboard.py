from flask import Blueprint, jsonify, request
from src.utils import connect_to_mongodb, close_mongodb_connection

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
            if request.path == '/api/login':
                return jsonify({'message': 'Login successful'}), 200
            elif request.path == '/api/private':
                return jsonify({'message': 'Private access granted'}), 200
        else:
            return jsonify({'error': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
