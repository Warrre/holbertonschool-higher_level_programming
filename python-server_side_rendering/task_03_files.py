import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products(path):
    """Read products from a JSON file and return a list of dicts."""
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return data
            # sometimes wrapped in a dict with key 'products'
            if isinstance(data, dict) and 'products' in data and isinstance(data['products'], list):
                return data['products']
    except Exception:
        pass
    return []


def read_csv_products(path):
    """Read products from a CSV file and return a list of dicts."""
    products = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # normalize fields and convert id and price
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


@app.route('/products')
def products():
    """Render products from JSON or CSV based on ?source= and optional ?id=."""
    source = request.args.get('source', 'json').lower()
    id_param = request.args.get('id')

    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'products.json')
    csv_path = os.path.join(base_dir, 'products.csv')

    error = None
    products_list = []

    if source == 'json':
        products_list = read_json_products(json_path)
    elif source == 'csv':
        products_list = read_csv_products(csv_path)
    else:
        error = 'Wrong source'

    # Normalize products list: ensure ids are ints and price is displayed nicely
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
