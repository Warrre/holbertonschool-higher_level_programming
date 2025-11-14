import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    """Read items from items.json and render items.html with the list."""
    # Locate items.json relative to this file
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'items.json')

    items_list = []
    try:
        with open(json_path, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
            # Expecting a dict with key "items" mapping to a list
            if isinstance(data, dict) and 'items' in data and isinstance(data['items'], list):
                items_list = data['items']
            else:
                # If structure is unexpected, fallback to empty list
                items_list = []
    except FileNotFoundError:
        # If the JSON file doesn't exist, pass empty list and template will show message
        items_list = []
    except Exception:
        # Any other error reading/parsing -> empty list
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
