from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
employees_collection = db["employees"]

@app.route('/employees', methods=['POST'])
def add_employee_to_campaign():
    data = request.json
    employee = {
        "campaign_id": data['campaign_id'],
        "employee_id": data['employee_id']
    }
    result = employees_collection.insert_one(employee)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/employees/<campaign_id>', methods=['GET'])
def get_employees(campaign_id):
    employees = list(employees_collection.find({"campaign_id": campaign_id}))
    for employee in employees:
        employee["_id"] = str(employee["_id"])
    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
