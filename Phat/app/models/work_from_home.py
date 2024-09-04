from pymongo import MongoClient

class WorkFromHomeModel:
    def __init__(self, mongo_client):
        self.db = mongo_client.staff_management
        self.collection = self.db.work_from_home_requests

    def create_request(self, request_data):
        return self.collection.insert_one(request_data).inserted_id

    def get_request_by_id(self, request_id):
        return self.collection.find_one({"_id": request_id})

    def update_request(self, request_id, update_data):
        return self.collection.update_one({"_id": request_id}, {"$set": update_data})

    def get_all_requests(self):
        return list(self.collection.find())
