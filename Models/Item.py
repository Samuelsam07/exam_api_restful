from config import db

class Item (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = True)
    weight = db.Column(db.Float, nullable = True)
    description = db.Column(db.String, nullable = True)
