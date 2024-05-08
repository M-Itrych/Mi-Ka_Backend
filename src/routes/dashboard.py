from flask import Blueprint, jsonify, request, Response
from src.utils import connect_to_mongodb, close_mongodb_connection

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/api/login', methods=['POST'])
def login():
    try:
        client, db = connect_to_mongodb()
        users = db.users
        authKey = list(users.find({'authKey': str(request.authorization)}))
        close_mongodb_connection(client)
        if authKey:
            return jsonify({'error': 'Authentication successful'}), 200
        else:
            return jsonify({'error': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
