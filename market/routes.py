from market import app, db
from flask import render_template, url_for, redirect, flash
from market.models import Item, Users
from market.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route("/")
def home_page():
    return render_template("home.html", title= "homePage")

@app.route('/market')
@login_required
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

        login_user(new_user)
        flash("You have succesfully created your account", category="success")

        return redirect(url_for('market_page'))
    if form.errors != {}:
       for err_msg in form.errors.values():
           flash(f'an error occur: {err_msg[0]}', category='danger')
    
    return render_template('register.html',title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        print(attempted_user, form.username.data)
        if attempted_user:
            if attempted_user.check_password(form.password.data):
                login_user(attempted_user)
                flash('You sucessfully login into your account', category='success')
                return redirect(url_for('market_page'))
            else:
                flash('bad password, please provide the right one', category='danger')
        else:
            flash('bad username, please provide the right one', category='danger')
    return render_template('login.html', form = form)


@app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    flash("You have been logged out", category="info")
    return redirect(url_for('home_page'))