from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Hello_world():
    return render_template("home.html", title= "homePage")

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode':'893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode':'123212299165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode':'231922998446', 'price': 150}
    ]
    return render_template('market.html', title='market page', items = items)