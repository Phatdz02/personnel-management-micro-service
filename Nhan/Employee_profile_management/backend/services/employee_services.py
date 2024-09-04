from models.employee import EmployeeModel

class EmployeeService:
    def __init__(self):
        self.employee_model = EmployeeModel()

    def create_employee(self, data):
        return self.employee_model.create_employee(data)

    def update_employee(self, employee_id, data):
        return self.employee_model.update_employee(employee_id, data)

    def delete_employee(self, employee_id):
        return self.employee_model.delete_employee(employee_id)

    def search_employee(self, query):
        return self.employee_model.search_employee(query)

    def view_employee(self, employee_id):
        return self.employee_model.view_employee(employee_id)
