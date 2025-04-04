from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app)  # Enable CORS for all routes

    # Import and register blueprints
    from flask_api.routes import api_bp
    app.register_blueprint(api_bp)

    return app