from config import db
from Customer import Customer

class Order (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    createDate = db.Column(db.Date, nullable = True)


    CustomerId = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = True)
    customer = db.relationship('Customers', foreign_keys = [CustomerId])
