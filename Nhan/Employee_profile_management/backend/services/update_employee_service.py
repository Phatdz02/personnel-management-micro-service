from flask import Flask
from routes.update_employee_routes import update_employee_blueprint

app = Flask(__name__)
app.register_blueprint(update_employee_blueprint)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
