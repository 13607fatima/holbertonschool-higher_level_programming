import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            target_id = int(product_id)
            data = [p for p in data if p['id'] == target_id]
            if not data:
                return render_template('product_display.html',
                                       error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid ID format")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
