from app.models.timecard_update import TimecardUpdateModel

class TimecardService:
    def __init__(self, mongo_client):
        self.model = TimecardUpdateModel(mongo_client)

    def create_timecard_update(self, update_data):
        # Implement validation and logic
        return self.model.create_update(update_data)

    def get_timecard_update(self, update_id):
        return self.model.get_update_by_id(update_id)

    def update_timecard_update(self, update_id, update_data):
        return self.model.update_update(update_id, update_data)

    def get_all_timecard_updates(self):
        return self.model.get_all_updates()
