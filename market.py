from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Hello_world():
    return render_template("home.html", title= "homePage")

@app.route('/market')
def market_page():
    return render_template('market.html', title="marketPage")