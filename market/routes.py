from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route("/")
def Hello_world():
    return render_template("home.html", title= "homePage")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', title='market page', items = items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)