from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
activities_collection = db["activities"]

@app.route('/activities', methods=['GET'])
def get_activities():
    activities = list(activities_collection.find())
    for activity in activities:
        activity["_id"] = str(activity["_id"])
    return jsonify(activities)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
