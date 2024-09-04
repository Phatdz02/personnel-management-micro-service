from app.models.leave_request import LeaveRequestModel

class LeaveService:
    def __init__(self, mongo_client):
        self.model = LeaveRequestModel(mongo_client)

    def create_leave_request(self, request_data):
        # Implement validation and logic
        return self.model.create_request(request_data)

    def get_leave_request(self, request_id):
        return self.model.get_request_by_id(request_id)

    def update_leave_request(self, request_id, update_data):
        return self.model.update_request(request_id, update_data)

    def get_all_leave_requests(self):
        return self.model.get_all_requests()
