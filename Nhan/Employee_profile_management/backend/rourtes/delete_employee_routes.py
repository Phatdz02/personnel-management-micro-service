from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_service = EmployeeService()
delete_employee_blueprint = Blueprint('delete_employee', __name__)

@delete_employee_blueprint.route('/delete/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    success = employee_service.delete_employee(employee_id)
    if success:
        return jsonify({'message': 'Employee deleted successfully'}), 200
    else:
        return jsonify({'message': 'Employee not found'}), 404
