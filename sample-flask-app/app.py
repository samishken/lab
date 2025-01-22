from flask import Flask
from routes.flashcards import flashcards_bp
from models.database import db
import os

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object("config.Config")

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(flashcards_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

