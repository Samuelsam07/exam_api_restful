from app import app
from config import db
from Models.Customer import Customer
from Models.order import Order
from Models.OrderDetail import OrderDetail
from Models.OrederStatus import OrderStatus
from Models.Payement import Payment
from Models.Item import Item
from flask import Flask, request, jsonify, render_template
from Models.check import Check
from Models.credit import Credit 
from Models.cash import Cash
from Models.wireTransfer import WireTransfer






with app.app_context():
    db.create_all()
     

@app.route('/customer/add', methods = ['POST'])
def customer_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']

        if name and deliveryAddress and contact and active and request.method == 'POST':
           
            print(" -------------- ")
            customers = Customer(name = name, deliveryAddress = deliveryAddress, contact = contact, active = active)

            db.session.add(customers)
            db.session.commit()
            resultat = jsonify('Customer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()



@app.route('/customer', methods = ['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        data = [{"id":customers.id, "name":customers.name, "deliveryAddress":customers.deliveryAddress, "contact":customers.contact, "active":customers.active} for customers in customers]

        resultat = jsonify({"status_code":200, "Customer" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
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


@app.route('/order', methods = ['GET'])
def get_order():
    try:
        orders = Order.query.all()
        data = [{"id":order.id, "createData":order.createData} for order in orders]

        resultat = jsonify({"status_code":200, "Orders" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
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

@app.route('/orderDetail', methods = ['GET'])
def orderDetail():
    try:
        orderDetails = OrderDetail.query.all()
        data = [{"id":orderDetail.id, "qty":orderDetail.qty, "taxStatus":orderDetail.taxStatus} for orderDetail in orderDetails]
        resultat = jsonify({"status_code":200, "OrderDetail" : data})
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
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
        
@app.route('/payement', methods = ['GET'])
def get_payement():
    try:
        payements = Payment.query.all()
        data = [{"id":payement.id, "name":payement.name} for payement in payements]

        resultat = jsonify({"status_code":200, "Payement" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
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

@app.route('/items', methods = ['GET'])
def get_items():
    try:
        items = Item.query.all()
        data = [{"id":item.id, "weight":item.weight, "description":item.description} for item in items]

        resultat = jsonify({"status_code":200, "Item" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/orderStatus/add', methods = ['POST'])
def orderstatus_add():
    try:
        json = request.json
        print(json)
        CREATE = json['CREATE']
        SHIPPING = json['SHIPPING']
        DELIVERED = json['DELIVERED']
        PAID = json['PAID']

        if CREATE and SHIPPING and DELIVERED and PAID and request.method == 'POST':
           
            print(" -------------- ")

            orderStatus = OrderStatus(CREATE = CREATE, SHIPPING = SHIPPING, DELIVERED = DELIVERED, PAID = PAID)

            db.session.add(orderStatus)
            db.session.commit()
            resultat = jsonify('Order Status add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


@app.route('/check/add', methods = ['POST'])
def check_add():
    try:
        json = request.json
        print(json)
        name = json['name']
        bankID = json['bankID']

        if name and bankID and request.method == 'POST':
           
            print(" -------------- ")
            
            checks = Check(name = name, bankID = bankID)

            db.session.add(checks)
            db.session.commit()
            resultat = jsonify('New Check add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


@app.route('/wiretransfer/add', methods = ['POST'])
def wiretransfer_add():
    try:
        json = request.json
        print(json)
        bankID = json['bankID']
        bankName = json['bankName']

        if bankID and bankName and request.method == 'POST':
           
            print(" -------------- ")
            
            wiretransfer = WireTransfer(bankID = bankID, bankName = bankName)

            db.session.add(wiretransfer)
            db.session.commit()
            resultat = jsonify('New Wire Transfer add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


@app.route('/Cash/add', methods = ['POST'])
def cash_add():
    try:
        json = request.json
        print(json)
        cashTendered = json['cashTendered']

        if cashTendered and request.method == 'POST':
           
            print(" -------------- ")
            
            cashs = Cash(cashTendered = cashTendered)

            db.session.add(cashs)
            db.session.commit()
            resultat = jsonify('New Cash add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()


@app.route('/cash', methods = ['GET'])
def get_cash():
    try:
        cashs = Customer.query.all()
        data = [{"id":cash.id, "number":cash.number} for cash in cashs]

        resultat = jsonify({"status_code":200, "cash" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/credit/add', methods = ['POST'])
def credit_add():
    try:
        json = request.json
        print(json)
        number = json['number']
        types = json['types']
        expireDate = json['expireDate']

        if number and types and expireDate and request.method == 'POST':
           
            print(" -------------- ")
            credits = Credit(number = number, types = types, expireDate = expireDate)

            db.session.add(credits)
            db.session.commit()
            resultat = jsonify('New Credit add')
            return resultat

    except Exception as e :
        print(e)
        resultat = {"code_status" : 404, "message" : "Error"}
        return jsonify(resultat)
    finally :
        db.session.rollback()
        db.session.close()

@app.route('/credit', methods = ['GET'])
def get_credit():
    try:
        credits = Customer.query.all()
        data = [{"id":credit.id, "number":credit.number, "type":credit.type, "expireDate":credit.expireDate} for credit in credits]

        resultat = jsonify({"status_code":200, "credit" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


if(__name__ == '__main__'):
    app.run(debug=True, host= "0.0.0.0", port= 2000)    