from pymongo import MongoClient

class TimecardUpdateModel:
    def __init__(self, mongo_client):
        self.db = mongo_client.staff_management
        self.collection = self.db.timecard_updates

    def create_update(self, update_data):
        return self.collection.insert_one(update_data).inserted_id

    def get_update_by_id(self, update_id):
        return self.collection.find_one({"_id": update_id})

    def update_update(self, update_id, update_data):
        return self.collection.update_one({"_id": update_id}, {"$set": update_data})

    def get_all_updates(self):
        return list(self.collection.find())
