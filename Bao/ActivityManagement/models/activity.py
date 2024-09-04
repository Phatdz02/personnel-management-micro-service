from pymongo import MongoClient

class ActivityModel:
    def __init__(self):
        self.client = MongoClient("mongodb://mongodb:27017/")
        self.db = self.client['activity_db']
        self.collection = self.db['activities']

    def create_activity(self, name, distance, duration, start_date, end_date):
        activity_data = {
            "name": name,
            "distance": distance,
            "duration": duration,
            "start_date": start_date,
            "end_date": end_date
        }
        self.collection.insert_one(activity_data)
        return activity_data
    
    def insert_activity(self, activity_data):
        self.collection.insert_one(activity_data)

    def get_activities(self, query={}):
        return list(self.collection.find(query))

    def save_strava_account(self, user_id, access_token, refresh_token, expires_at):
        account_data = {
            "user_id": user_id,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at
        }
        self.collection.update_one(
            {"user_id": user_id},
            {"$set": account_data},
            upsert=True
        )