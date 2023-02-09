from config import db

class OrderDetail (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    qty = db.Column(db.Integer, nullable = True)
    taxStatus = db.Column(db.String, nullable = True)
