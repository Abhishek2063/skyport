from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from ..extensions import db

class Aircraft(db.Model):
    __tablename__ = 'aircrafts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)         # Model name
    code = db.Column(db.String(20), nullable=False, unique=True)  # Unique code (e.g., B737)
    total_seats = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Aircraft {self.code} - {self.name}>"

    flights = db.relationship('Flight', backref='aircraft', lazy=True)