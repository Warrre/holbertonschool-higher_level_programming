import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

# Ensure Flask finds templates when imported by external checkers
_BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__, template_folder=os.path.join(_BASE_DIR, 'templates'))


def read_json_products(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and 'products' in data and isinstance(data['products'], list):
                return data['products']
    except Exception:
        pass
    return []


def read_csv_products(path):
    products = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    pid = int(row.get('id') or row.get('ID') or 0)
                except Exception:
                    pid = None
                name = row.get('name') or row.get('Name') or ''
                category = row.get('category') or row.get('Category') or ''
                try:
                    price = float(row.get('price') or row.get('Price') or 0)
                except Exception:
                    price = None
                products.append({'id': pid, 'name': name, 'category': category, 'price': price})
    except Exception:
        pass
    return products


def read_sql_products(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT id, name, category, price FROM Products')
        rows = cur.fetchall()
        for r in rows:
            products.append({'id': r['id'], 'name': r['name'], 'category': r['category'], 'price': r['price']})
    except Exception:
        # Any DB error -> return empty list (caller may set error)
        products = []
    finally:
        try:
            conn.close()
        except Exception:
            pass
    return products


@app.route('/products')
def products():
    """Render products from JSON, CSV or SQL based on ?source= and optional ?id=."""
    source = request.args.get('source', 'json').lower()
    id_param = request.args.get('id')

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'products.json')
    csv_path = os.path.join(base_dir, 'products.csv')
    db_path = os.path.join(base_dir, 'products.db')

    error = None
    products_list = []

    if source == 'json':
        products_list = read_json_products(json_path)
    elif source == 'csv':
        products_list = read_csv_products(csv_path)
    elif source == 'sql' or source == 'sqlite' or source == 'db':
        # attempt to read from SQLite database
        if not os.path.exists(db_path):
            error = 'Product not found'
        else:
            try:
                products_list = read_sql_products(db_path)
            except Exception:
                products_list = []
    else:
        error = 'Wrong source'

    # Normalize products list
    normalized = []
    for p in products_list:
        try:
            pid = int(p.get('id')) if p.get('id') is not None else None
        except Exception:
            pid = None
        try:
            price = float(p.get('price')) if p.get('price') is not None else None
        except Exception:
            price = None
        normalized.append({'id': pid, 'name': p.get('name', ''), 'category': p.get('category', ''), 'price': price})

    # If id provided, filter
    if error is None and id_param is not None:
        try:
            target_id = int(id_param)
        except Exception:
            error = 'Product not found'
            target_id = None

        if error is None:
            filtered = [p for p in normalized if p['id'] == target_id]
            if not filtered:
                error = 'Product not found'
            else:
                normalized = filtered

    return render_template('product_display.html', products=normalized, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
