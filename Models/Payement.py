from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable  = False)
    
    
    _mapper_args_ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': 'payment_mode'
    }


    ## OneToMany de Order vers payment
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])



