from flask import Flask
from .extensions import db, jwt, migrate,bcrypt
from .config import Config
from .routes.auth import auth_bp

# 🚨 Import models so they are registered before migrations
from .models.user import User
from .models.role import Role
from .models.airport import Airport
from .models.aircraft import Aircraft
from .models.flight import Flight
from .models.booking import Booking
from .models.payment import Payment

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
