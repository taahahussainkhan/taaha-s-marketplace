from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')
@app.route('/market')
def market_page():
    items = [
        { 'id' : 1, 'name' : 'Phone', 'barcode': '893212299897', 'price' : 500},
        { 'id' : 2, 'name' : 'Laptop', 'barcode': '893212296827', 'price' : 1500},
        { 'id' : 3, 'name' : 'Tablet', 'barcode': '893212292894', 'price' : 600},
        { 'id' : 4, 'name' : 'Headphones', 'barcode': '893212299895', 'price' : 400}
    ] 
    return render_template('market.html',items = items)

app.run(debug=True)