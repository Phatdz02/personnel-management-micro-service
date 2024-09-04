from flask import Flask
from routes.delete_employee_routes import delete_employee_blueprint

app = Flask(__name__)
app.register_blueprint(delete_employee_blueprint)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
