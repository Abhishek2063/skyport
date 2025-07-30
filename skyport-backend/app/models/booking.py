from datetime import datetime
from ..extensions import db


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
    booking_code = db.Column(db.String(20), unique=True, nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')  # Confirmed / Cancelled / Pending
    booked_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships (optional, for convenience)
    user = db.relationship('User', back_populates='bookings', lazy=True)
    flight = db.relationship('Flight', back_populates='bookings', lazy=True)
    payment = db.relationship('Payment', backref='booking', uselist=False)
    def __repr__(self):
        return f"<Booking {self.booking_code}>"
