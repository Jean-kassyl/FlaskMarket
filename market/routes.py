from market import app, db
from flask import render_template, url_for, redirect, flash
from market.models import Item, Users
from market.forms import RegisterForm, LoginForm

@app.route("/")
def Hello_world():
    return render_template("home.html", title= "homePage")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', title='market page', items = items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(username=form.username.data, user_email=form.email.data, password=form.password1.data)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('market_page'))
    if form.errors != {}:
       for err_msg in form.errors.values():
           flash(f'an error occur: {err_msg[0]}', category='danger')
    
    return render_template('register.html',title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form = form)