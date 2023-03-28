from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, Form
from app.models import User, Product, CartItem, ProductQuantity

@app.route('/')
@login_required
def index():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>/', methods=['GET', 'POST'])
@login_required
def product(product_id):
    product = Product.query.get_or_404(product_id)
    product_quantitys = ProductQuantity.query.filter_by(product_id=product_id).all()
    # form = Form()
    
    choices = [(item.product_id, item.size, item.price) for item in product_quantitys]
    price_list = [z for x,y,z in choices]
    return render_template('products.html', product_id=product.id, product=product, choices=choices, price_list=price_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        # user.set_email(form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total_price = sum([item.price for item in cart_items])
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add_to_cart/<int:product_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(product_id):
    # productquantity_id = ProductQuantity.query.filter()
    product_id = request.form['product_id']
    price = request.form['price'][1:]
    productquantity_id = ProductQuantity.query.filter_by(price=price, product_id=product_id).first().id
    # price = request.form['price']
    item = CartItem(user_id=current_user.id, product_id=product_id, price=price, productquantity_id=productquantity_id)
    db.session.add(item)
    db.session.commit()
    flash('Item added to cart')
    # return request.form['product_id']
    return redirect(url_for('cart'))




#    <!-- <form action="{{ url_for('checkout') }}" method="post">
#       <input type="submit" value="Checkout">
#     </form> -->