from flask import Flask
from config import ProductionConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    from .webhook.routes import webhook_bp
    app.register_blueprint(webhook_bp)

    return app