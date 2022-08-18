from datetime import timedelta

from flask import Flask

from app.web.environment import settings
from app.web.globals import STATIC_PATH, TEMPLATE_PATH
from app.web.views import router

# In a more complex app we'd have multiple blueprints for different routes.
BLUEPRINTS = [
    # (BLUEPRINT, PREFIX),
    (router, "")
]


def register_blueprints(app: Flask) -> None:
    """Register app blueprints with url prefix locations"""
    for blueprint, prefix in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix=prefix)


def set_app_config(app: Flask) -> None:
    """Set app config items from environment variables"""
    # Flask stuff
    app.config["SECRET_KEY"] = settings.secret_key
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # 16 MB
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(days=365)


def create_app() -> Flask:
    """Create the Flask app and set its configuration"""

    # Initiate app
    app = Flask(
        __name__,
        template_folder=str(TEMPLATE_PATH),
        static_folder=str(STATIC_PATH),
    )

    # Update config from environment variables
    set_app_config(app)

    # Register blueprints
    register_blueprints(app)

    return app
