import os
import requests
from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
from os import path
from snap_financial_factors.benefit_estimate.snap_estimate_entrypoint import SnapEstimateEntrypoint


def create_app():
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    if path.exists(".env"):
        from dotenv import load_dotenv
        load_dotenv()

    @auth.verify_password
    def verify_password(username, password):
        # Auth not required locally, just in production.
        # Setting an AUTH_OFF flag to any value will turn off auth.
        auth_off = os.getenv('AUTH_OFF', False)

        if auth_off:
            return True

        # If auth is on, a username and password must be supplied
        # as environment variables.
        env_username = os.environ['USERNAME']
        env_password = os.environ['PASSWORD']

        if (username == env_username) and (password == env_password):
            return True

        return False

    @app.route('/')
    @auth.login_required
    def get_root():
        return render_template('prescreener.html')

    @app.route('/calculate', methods=['POST'])
    @auth.login_required
    def call_api():
        request_json_data = request.get_json()

        call_api_method = os.environ.get('CALL_API_METHOD', 'PYTHON_LIBRARY')

        if call_api_method == 'PYTHON_LIBRARY':
            return SnapEstimateEntrypoint(request_json_data).calculate()
        elif call_api_method == 'WEB_API':
            api_username = os.environ['API_USERNAME']
            api_password = os.environ['API_PASSWORD']
            api_url = os.environ['API_URL']

            response = requests.post(
                api_url,
                json=request_json_data,
                auth=(api_username, api_password)
            ).json()

            return response
        else:
            raise ValueError("Unknown method for calling API.")

    return app
