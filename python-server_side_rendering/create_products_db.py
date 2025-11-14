import sqlite3
import os


def create_database(db_path=None):
    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Insert sample data; use INSERT OR IGNORE in case rows already exist
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price) VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Wireless Mouse', 'Electronics', 29.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
    print('products.db created/updated')
