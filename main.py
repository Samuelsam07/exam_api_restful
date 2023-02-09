from app import app
from config import db
from Customer import Customer
from order import Order
from OrderDetail import OrderDetail
#from OrederStatus import OrederStatus
from Payement import Payement
from Item import Item
from flask import Flask, request, jsonify, render_template

with app.app_context():
    db.create_all()
     

@app.route('/Customer/add', methods = ['POST'])
def add_customer():
    try:
        json = request.json
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']

        if name and deliveryAddress and contact and request.method == 'POST':
            customers = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)
            db.session.add(customers)
            db.session.commit()
            resultat = jsonify('client ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()



@app.route('/Order/add', methods = ['POST'])
def add_Order():
    try:
        json = request.json
        createDate = json['createDate']
        

        if createDate  and request.method == 'POST':
            Order = Order(createDate = createDate)
            db.session.add(Order)
            db.session.commit()
            resultat = jsonify('Ordre ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
        

@app.route('/OrderDetail/add', methods = ['POST'])
def add_OrderDetail():
    try:
        json = request.json
        qty = json['qty']
        taxStatus = json['taxStatus']
        

        if qty  and taxStatus and request.method == 'POST':
            OrderDetail = OrderDetail(qty = qty)
            OrderDetail = OrderDetail(taxStatus = taxStatus)
            db.session.add(OrderDetail)
            db.session.commit()
            resultat = jsonify('OrderDetail ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/Payement/add', methods = ['POST'])
def add_Payement():
    try:
        json = request.json
        amount = amount['qty']
        

        if amount and request.method == 'POST':
            Payement = Payement(amount = amount)
            db.session.add(Payement)
            db.session.commit()
            resultat = jsonify('Payement ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()




@app.route('/Item/add', methods = ['POST'])
def add_Item():
    try:
        json = request.json
        weight = json['weight']
        description = json['description']
        

        if weight  and description and request.method == 'POST':
            Item = Item(weight = weight)
            Item = Item(description = description)
            db.session.add(Item)
            db.session.commit()
            resultat = jsonify('Item ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/OrderStatus/add', methods = ['POST'])
def add_OrderStatus():
    try:
        json = request.json
        qty = json['qty']
        taxStatus = json['taxStatus']
        

        if qty  and taxStatus and request.method == 'POST':
            OrderStatus = OrderStatus(qty = qty)
            OrderStatus = OrderStatus(taxStatus = taxStatus)
            db.session.add(OrderStatus)
            db.session.commit()
            resultat = jsonify('OrderStatus ajoute')
            return resultat

    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()

if(__name__ == '__main__'):
    app.run(debug=True, host= "0.0.0.0", port= 2000)    