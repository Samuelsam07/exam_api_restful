from config import db
from Models.Customer import Customer

class Order (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    createDate = db.Column(db.Date, nullable = True)


   ## OneToMany de Customer vers Order
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = True)
    customer = db.relationship('Customer', foreign_keys = [customerId])

