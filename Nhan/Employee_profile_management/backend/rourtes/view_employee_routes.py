from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_service = EmployeeService()
view_employee_blueprint = Blueprint('view_employee', __name__)

@view_employee_blueprint.route('/view/<employee_id>', methods=['GET'])
def view_employee(employee_id):
    employee = employee_service.view_employee(employee_id)
    if employee:
        employee['_id'] = str(employee['_id'])
        return jsonify(employee)
    else:
        return jsonify({'message': 'Employee not found'}), 404
