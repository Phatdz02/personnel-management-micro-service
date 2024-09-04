from flask import Flask
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes.create_employee_routes import create_employee_blueprint

app = Flask(__name__)
app.register_blueprint(create_employee_blueprint)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
