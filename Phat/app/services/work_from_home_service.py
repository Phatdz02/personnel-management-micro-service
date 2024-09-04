from app.models.work_from_home import WorkFromHomeModel

class WorkFromHomeService:
    def __init__(self, mongo_client):
        self.model = WorkFromHomeModel(mongo_client)

    def create_work_from_home_request(self, request_data):
        # Implement validation and logic
        return self.model.create_request(request_data)

    def get_work_from_home_request(self, request_id):
        return self.model.get_request_by_id(request_id)

    def update_work_from_home_request(self, request_id, update_data):
        return self.model.update_request(request_id, update_data)

    def get_all_work_from_home_requests(self):
        return self.model.get_all_requests()
