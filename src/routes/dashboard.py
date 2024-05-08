from flask import Blueprint, jsonify, request, Response
from src.utils import connect_to_mongodb, close_mongodb_connection, serialize_id
from bson.objectid import ObjectId

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/api/login', methods=['POST'])
def login():
    try:
        if request.authorization and request.authorization.username == '123' and request.authorization.password == '123':
            print(request.authorization.username, request.authorization.password)
            return jsonify({'message': 'Authentication successful'}), 200
        else:
            return jsonify({'error': 'Authentication failed'}), 401
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
