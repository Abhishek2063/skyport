from datetime import datetime
from sqlalchemy import DECIMAL
from ..extensions import db

class Flight(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    
    flight_number = db.Column(db.String(20), nullable=False, unique=True)

    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircrafts.id'), nullable=False)
    departure_airport_id = db.Column(db.Integer, db.ForeignKey('airports.id'), nullable=False)
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey('airports.id'), nullable=False)

    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)

    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Base price
    status = db.Column(db.String(20), nullable=False, default='Scheduled')  # Scheduled / Cancelled / Delayed

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    bookings = db.relationship('Booking', back_populates='flight')

    departure_airport = db.relationship(
        'Airport',
        foreign_keys=[departure_airport_id],
        back_populates='departing_flights'
    )

    arrival_airport = db.relationship(
        'Airport',
        foreign_keys=[arrival_airport_id],
        back_populates='arriving_flights'
    )

    aircraft = db.relationship(
        'Aircraft',
        back_populates='flights'
    )

    def __repr__(self):
        return f"<Flight {self.flight_number}>"


