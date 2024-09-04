from flask import Blueprint, request, jsonify
from app.services.checkin_checkout_service import CheckinCheckoutService
from app.config import Config
from pymongo import MongoClient

checkin_checkout_routes = Blueprint('checkin_checkout_routes', __name__)
mongo_client = MongoClient(Config.MONGO_URI)
checkin_checkout_service = CheckinCheckoutService(mongo_client)

@checkin_checkout_routes.route('/checkin-checkout', methods=['POST'])
def create_checkin_checkout_entry():
    data = request.json
    entry_id = checkin_checkout_service.create_checkin_checkout_entry(data)
    return jsonify({"entry_id": str(entry_id)}), 201

@checkin_checkout_routes.route('/checkin-checkout/<entry_id>', methods=['GET'])
def get_checkin_checkout_entry(entry_id):
    checkin_checkout_entry = checkin_checkout_service.get_checkin_checkout_entry(entry_id)
    return jsonify(checkin_checkout_entry), 200

@checkin_checkout_routes.route('/checkin-checkout/<entry_id>', methods=['PUT'])
def update_checkin_checkout_entry(entry_id):
    data = request.json
    checkin_checkout_service.update_checkin_checkout_entry(entry_id, data)
    return jsonify({"message": "Check-in/Check-out entry updated successfully"}), 200

@checkin_checkout_routes.route('/checkin-checkouts', methods=['GET'])
def get_all_checkin_checkout_entries():
    checkin_checkout_entries = checkin_checkout_service.get_all_checkin_checkout_entries()
    return jsonify(checkin_checkout_entries), 200
