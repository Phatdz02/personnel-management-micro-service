from flask import Blueprint, request, jsonify
from ActivityManagement.models.activity import ActivityModel
from ActivityManagement.services.strava_services import StravaService

activity_bp = Blueprint('activity', __name__)
activity_model = ActivityModel()

@activity_bp.route('/activities/create', methods=['POST'])
def create_activity():
    data = request.json
    name = data.get('name')
    distance = data.get('distance')
    duration = data.get('duration')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not all([name, distance, duration, start_date, end_date]):
        return jsonify({"error": "Missing required fields"}), 400

    new_activity = activity_model.create_activity(name, distance, duration, start_date, end_date)
    return jsonify(new_activity), 201

@activity_bp.route('/activities', methods=['POST'])
def fetch_and_store_activities():
    access_token = request.json.get('access_token')
    stra_service = StravaService(access_token)
    activities = stra_service.get_activities()
    
    for activity in activities:
        activity_model.insert_activity(activity)
    
    return jsonify({"message": "Activities stored successfully"}), 201

@activity_bp.route('/activities', methods=['GET'])
def get_activities():
    activities = activity_model.get_activities()
    return jsonify(activities), 200
