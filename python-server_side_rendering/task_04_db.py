from flask import Flask, render_template, request
import json, csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    products_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error_message='Wrong source')
    if source == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
            products_list = data
    elif source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products_list = list(reader)
    elif source == 'sql':
        connect = sqlite3.connect('products.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products_list = []
        for row in rows:
            product_dict = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products_list.append(product_dict)
        connect.close()
    if products_id:
        filtered_products = [p for p in products_list if str(p.get('id')) == products_id]
        if not filtered_products:
            return render_template('product_display.html',
                                   error_message="Product not found")
        products_list = filtered_products
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
