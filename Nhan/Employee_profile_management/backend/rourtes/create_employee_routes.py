from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_service = EmployeeService()
create_employee_blueprint = Blueprint('create_employee', __name__)

@create_employee_blueprint.route('/create', methods=['POST'])
def create_employee():
    data = request.json
    employee_id = employee_service.create_employee(data)
    return jsonify({'message': 'Employee created', 'id': str(employee_id)}), 201
