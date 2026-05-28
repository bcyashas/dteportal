from flask import Flask
from .extensions import db
from .routes.auth import auth_bp
from .routes.dashboard import dashboard_bp
from .routes.profile import profile_bp
from .routes.task import task_bp
from config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(task_bp)
    return app
from flask import render_template

