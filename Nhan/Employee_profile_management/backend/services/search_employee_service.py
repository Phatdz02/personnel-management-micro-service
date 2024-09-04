from flask import Flask
from routes.search_employee_routes import search_employee_blueprint

app = Flask(__name__)
app.register_blueprint(search_employee_blueprint)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
