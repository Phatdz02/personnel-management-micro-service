from flask import Blueprint, request, jsonify
from app.services.work_from_home_service import WorkFromHomeService
from app.config import Config
from pymongo import MongoClient

work_from_home_routes = Blueprint('work_from_home_routes', __name__)
mongo_client = MongoClient(Config.MONGO_URI)
work_from_home_service = WorkFromHomeService(mongo_client)

@work_from_home_routes.route('/work-from-home', methods=['POST'])
def create_work_from_home_request():
    data = request.json
    request_id = work_from_home_service.create_work_from_home_request(data)
    return jsonify({"request_id": str(request_id)}), 201

@work_from_home_routes.route('/work-from-home/<request_id>', methods=['GET'])
def get_work_from_home_request(request_id):
    work_from_home_request = work_from_home_service.get_work_from_home_request(request_id)
    return jsonify(work_from_home_request), 200

@work_from_home_routes.route('/work-from-home/<request_id>', methods=['PUT'])
def update_work_from_home_request(request_id):
    data = request.json
    work_from_home_service.update_work_from_home_request(request_id, data)
    return jsonify({"message": "Work from home request updated successfully"}), 200

@work_from_home_routes.route('/work-from-home-requests', methods=['GET'])
def get_all_work_from_home_requests():
    work_from_home_requests = work_from_home_service.get_all_work_from_home_requests()
    return jsonify(work_from_home_requests), 200
