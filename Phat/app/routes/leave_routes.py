from flask import Blueprint, request, jsonify
from app.services.leave_service import LeaveService
from app.config import Config
from pymongo import MongoClient

leave_routes = Blueprint('leave_routes', __name__)
mongo_client = MongoClient(Config.MONGO_URI)
leave_service = LeaveService(mongo_client)

@leave_routes.route('/leave-request', methods=['POST'])
def create_leave_request():
    data = request.json
    leave_id = leave_service.create_leave_request(data)
    return jsonify({"leave_id": str(leave_id)}), 201

@leave_routes.route('/leave-request/<leave_id>', methods=['GET'])
def get_leave_request(leave_id):
    leave_request = leave_service.get_leave_request(leave_id)
    return jsonify(leave_request), 200

@leave_routes.route('/leave-request/<leave_id>', methods=['PUT'])
def update_leave_request(leave_id):
    data = request.json
    leave_service.update_leave_request(leave_id, data)
    return jsonify({"message": "Leave request updated successfully"}), 200

@leave_routes.route('/leave-requests', methods=['GET'])
def get_all_leave_requests():
    leave_requests = leave_service.get_all_leave_requests()
    return jsonify(leave_requests), 200
