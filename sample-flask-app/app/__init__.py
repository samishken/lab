from flask import Flask
from routes.flashcards import flashcards_bp
from models.database import db
from config import Config

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(flashcards_bp)

    return app
