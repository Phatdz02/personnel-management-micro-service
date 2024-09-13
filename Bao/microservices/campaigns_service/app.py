from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
campaigns_collection = db["campaigns"]

@app.route('/campaigns', methods=['POST'])
def create_campaign():
    data = request.json
    campaign = {
        "name": data['name'],
        "start_date": data['start_date'],
        "end_date": data['end_date']
    }
    result = campaigns_collection.insert_one(campaign)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/campaigns', methods=['GET'])
def get_campaigns():
    campaigns = list(campaigns_collection.find())
    for campaign in campaigns:
        campaign["_id"] = str(campaign["_id"])
    return jsonify(campaigns)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
