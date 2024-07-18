from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

def read_json(path_file):
    with open(path_file, 'r') as f:
        data = json.load(f)
    return data

def read_csv(path_file):
    data = []
    with open(path_file, 'r', new_line='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Source type not correct.")

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)