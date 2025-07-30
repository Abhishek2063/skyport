from datetime import datetime
from ..extensions import db

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # Card / UPI / Netbanking
    status = db.Column(db.String(20), nullable=False, default='Pending')  # Success / Failed / Pending
    paid_at = db.Column(db.DateTime, default=datetime.utcnow)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Optional relationship
    booking = db.relationship("Booking", back_populates="payment")

    def __repr__(self):
        return f"<Payment {self.id} - {self.status}>"
