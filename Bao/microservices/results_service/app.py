from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
results_collection = db["results"]

@app.route('/results', methods=['POST'])
def create_result():
    data = request.json
    result = {
        "employee_id": data['employee_id'],
        "campaign_id": data['campaign_id'],
        "distance": data.get('distance', None)
    }
    result = results_collection.insert_one(result)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/results', methods=['GET'])
def get_results():
    results = list(results_collection.find())
    for result in results:
        result["_id"] = str(result["_id"])
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
