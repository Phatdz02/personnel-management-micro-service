from flask import Flask
from ActivityManagement.routes.activity_routes import activity_bp
from flask import redirect, request, jsonify
import requests
import os
from ActivityManagement.models.activity import ActivityModel
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Đăng ký Blueprint cho các route
app.register_blueprint(activity_bp, url_prefix='/api')

activity_model = ActivityModel()

# Cấu hình OAuth2
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/api/strava/callback"

@app.route('/api/strava/connect')
def strava_connect():
    strava_auth_url = (
        f"https://www.strava.com/oauth/authorize?client_id={STRAVA_CLIENT_ID}"
        f"&response_type=code&redirect_uri={REDIRECT_URI}"
        f"&scope=activity:read_all,profile:read_all"
    )
    return redirect(strava_auth_url)

@app.route('/api/strava/callback')
def strava_callback():
    code = request.args.get('code')
    user_id = request.args.get('state')  # state có thể được dùng để truyền thông tin người dùng

    if not code:
        return jsonify({"error": "Authorization failed"}), 400

    # Yêu cầu access token từ Strava
    token_response = requests.post(
        "https://www.strava.com/oauth/token",
        data={
            "client_id": STRAVA_CLIENT_ID,
            "client_secret": STRAVA_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code"
        }
    ).json()

    access_token = token_response.get("access_token")
    refresh_token = token_response.get("refresh_token")
    expires_at = token_response.get("expires_at")

    # Lưu trữ token vào database
    activity_model.save_strava_account(user_id, access_token, refresh_token, expires_at)

    return jsonify({"message": "Strava account linked successfully"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)