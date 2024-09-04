import requests

class StravaService:
    def __init__(self, access_token):
        self.base_url = "https://www.strava.com/api/v3"
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def get_activities(self):
        response = requests.get(f"{self.base_url}/athlete/activities", headers=self.headers)
        return response.json()

    def get_activity_by_id(self, activity_id):
        response = requests.get(f"{self.base_url}/activities/{activity_id}", headers=self.headers)
        return response.json()
