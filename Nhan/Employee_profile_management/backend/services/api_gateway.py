from flask import Flask
import requests

app = Flask(__name__)

@app.route('/employee/create', methods=['POST'])
def create_employee():
    response = requests.post('http://localhost:5001/create', json=request.json)
    return response.json(), response.status_code

@app.route('/employee/update/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    response = requests.put(f'http://localhost:5002/update/{employee_id}', json=request.json)
    return response.json(), response.status_code

@app.route('/employee/delete/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    response = requests.delete(f'http://localhost:5003/delete/{employee_id}')
    return response.json(), response.status_code

@app.route('/employee/search', methods=['GET'])
def search_employee():
    response = requests.get('http://localhost:5004/search', params=request.args)
    return response.json(), response.status_code

@app.route('/employee/view/<employee_id>', methods=['GET'])
def view_employee(employee_id):
    response = requests.get(f'http://localhost:5005/view/{employee_id}')
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)
