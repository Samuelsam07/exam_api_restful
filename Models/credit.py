from config import db
from Models.Payement import Payment

class Credit(Payment):
    id = db.Column(db.Integer, primary_key = True , nullable = False )
    number  = db.Column(db.String(122), nullable = False )
    type = db.Column(db.String(122),nullable = False)
    expireDate  = db.Column(db.Date, nullable = False )
    
    __mapper_args__ = { 'polymorohic_identity':"Credit"}
