from pymongo import MongoClient
from bson.objectid import ObjectId

class EmployeeModel:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['employee_db']
        self.collection = self.db['profiles']

    def create_employee(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id

    def update_employee(self, employee_id, data):
        result = self.collection.update_one({'_id': ObjectId(employee_id)}, {'$set': data})
        return result.matched_count > 0

    def delete_employee(self, employee_id):
        result = self.collection.delete_one({'_id': ObjectId(employee_id)})
        return result.deleted_count > 0

    def search_employee(self, query):
        return self.collection.find({'$text': {'$search': query}})

    def view_employee(self, employee_id):
        return self.collection.find_one({'_id': ObjectId(employee_id)})
