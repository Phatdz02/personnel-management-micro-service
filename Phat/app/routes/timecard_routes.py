from flask import Blueprint, request, jsonify
from app.services.timecard_service import TimecardService
from app.config import Config
from pymongo import MongoClient

timecard_routes = Blueprint('timecard_routes', __name__)
mongo_client = MongoClient(Config.MONGO_URI)
timecard_service = TimecardService(mongo_client)

@timecard_routes.route('/timecard-update', methods=['POST'])
def create_timecard_update():
    data = request.json
    update_id = timecard_service.create_timecard_update(data)
    return jsonify({"update_id": str(update_id)}), 201

@timecard_routes.route('/timecard-update/<update_id>', methods=['GET'])
def get_timecard_update(update_id):
    timecard_update = timecard_service.get_timecard_update(update_id)
    return jsonify(timecard_update), 200

@timecard_routes.route('/timecard-update/<update_id>', methods=['PUT'])
def update_timecard_update(update_id):
    data = request.json
    timecard_service.update_timecard_update(update_id, data)
    return jsonify({"message": "Timecard update request updated successfully"}), 200

@timecard_routes.route('/timecard-updates', methods=['GET'])
def get_all_timecard_updates():
    timecard_updates = timecard_service.get_all_timecard_updates()
    return jsonify(timecard_updates), 200
