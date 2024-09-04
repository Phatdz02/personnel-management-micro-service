from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_service = EmployeeService()
search_employee_blueprint = Blueprint('search_employee', __name__)

@search_employee_blueprint.route('/search', methods=['GET'])
def search_employee():
    query = request.args.get('q', '')
    employees = employee_service.search_employee(query)
    results = []
    for employee in employees:
        employee['_id'] = str(employee['_id'])
        results.append(employee)
    return jsonify(results)
