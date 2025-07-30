from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import event
from ..extensions import db

class Airport(db.Model):
    __tablename__ = 'airports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)  # IATA code
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Airport {self.code} - {self.name}>"
    
    departing_flights = db.relationship('Flight', foreign_keys='Flight.departure_airport_id', back_populates='departure_airport')
    arriving_flights = db.relationship('Flight', foreign_keys='Flight.arrival_airport_id', back_populates='arrival_airport')
