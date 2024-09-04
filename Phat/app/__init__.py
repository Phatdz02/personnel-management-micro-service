from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.routes.leave_routes import leave_routes
from app.routes.timecard_routes import timecard_routes
from app.routes.checkin_checkout_routes import checkin_checkout_routes
from app.routes.work_from_home_routes import work_from_home_routes

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    
    app.register_blueprint(leave_routes, url_prefix='/api')
    app.register_blueprint(timecard_routes, url_prefix='/api')
    app.register_blueprint(checkin_checkout_routes, url_prefix='/api')
    app.register_blueprint(work_from_home_routes, url_prefix='/api')
    
    return app
