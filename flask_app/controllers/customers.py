from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.customer import Customer

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('create.html')


@app.route('/create',methods= ['POST'])
def create_customers():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email_address': request.form['email_address']   
    }
    Customer.new_customer(request.form)
    return redirect('/list_customers')


@app.route('/list_customers')
def display_all_customers():
    customers = Customer.get_all_customers()
    return render_template('readall.html', customers = customers)


@app.route('/select/<int:customer_id>/show')
def display_one_customer(customer_id):
    data = {
        'id' : customer_id
    }
    customer = Customer.get_customer_by_id(data)
    return render_template('readone.html', customer = customer)


@app.route('/select/<int:customer_id>/edit')
def edit_customer(customer_id):
    data = {
        'id': customer_id
    }
    customer = Customer.get_customer_by_id(data)
    print(customer)
    return render_template('edit_customer.html', customer = customer)


@app.route('/select/<int:customer_id>/update',methods= ['POST']) 
def update_customer(customer_id):
    data = {
        'id': customer_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email_address': request.form['email_address']   
    }
    Customer.update_one(data)
    return redirect(f"/select/{customer_id}/show")


@app.route('/select/<int:customer_id>/delete')
def delete_customer(customer_id):
    data = {
        'id': customer_id
    }
    Customer.delete_one(data)
    return redirect('/')
