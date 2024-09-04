from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_service = EmployeeService()
update_employee_blueprint = Blueprint('update_employee', __name__)

@update_employee_blueprint.route('/update/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    success = employee_service.update_employee(employee_id, data)
    if success:
        return jsonify({'message': 'Employee updated successfully'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404
