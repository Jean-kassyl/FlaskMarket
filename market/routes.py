from market import app
from flask import render_template
from market.models import Item

@app.route("/")
def Hello_world():
    return render_template("home.html", title= "homePage")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', title='market page', items = items)