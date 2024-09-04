from flask import Flask
from ..routes.view_employee_routes import view_employee_blueprint

app = Flask(__name__)
app.register_blueprint(view_employee_blueprint)

if __name__ == '__main__':
    app.run(port=5005, debug=True)
