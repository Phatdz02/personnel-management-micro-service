from app.models.checkin_checkout import CheckinCheckoutModel

class CheckinCheckoutService:
    def __init__(self, mongo_client):
        self.model = CheckinCheckoutModel(mongo_client)

    def create_checkin_checkout_entry(self, entry_data):
        # Implement validation and logic
        return self.model.create_entry(entry_data)

    def get_checkin_checkout_entry(self, entry_id):
        return self.model.get_entry_by_id(entry_id)

    def update_checkin_checkout_entry(self, entry_id, update_data):
        return self.model.update_entry(entry_id, update_data)

    def get_all_checkin_checkout_entries(self):
        return self.model.get_all_entries()
