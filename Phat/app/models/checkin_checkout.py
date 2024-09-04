from pymongo import MongoClient

class CheckinCheckoutModel:
    def __init__(self, mongo_client):
        self.db = mongo_client.staff_management
        self.collection = self.db.checkin_checkouts

    def create_entry(self, entry_data):
        return self.collection.insert_one(entry_data).inserted_id

    def get_entry_by_id(self, entry_id):
        return self.collection.find_one({"_id": entry_id})

    def update_entry(self, entry_id, update_data):
        return self.collection.update_one({"_id": entry_id}, {"$set": update_data})

    def get_all_entries(self):
        return list(self.collection.find())
