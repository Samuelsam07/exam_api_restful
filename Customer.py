from config import db


class Customer (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    name = db.Column(db.String, nullable = True)
    deliveryAddress = db.Column(db.String, nullable = True)
    contact = db.Column(db.String, nullable = True)
    active = db.Column(db.Boolean, nullable = True)

   