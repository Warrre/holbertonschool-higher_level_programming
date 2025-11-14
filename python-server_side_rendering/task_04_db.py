#!/usr/bin/env python3
"""
This module contains a Flask application that displays product data from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    """Read product data from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def read_csv_file():
    """Read product data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        return []
    except (ValueError, KeyError):
        return []
    return products


def read_sql_file():
    """Read product data from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
    except sqlite3.Error:
        return []
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/products')
def display_products():
    """Display products from JSON, CSV, or SQL based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error_message="Wrong source")
    
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        products = read_sql_file()
    
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', 
                                     error_message="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error_message="Product not found")
    
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
