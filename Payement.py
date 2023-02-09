from config import db

class Payement (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    amount = db.Column(db.Float, nullable = True)

