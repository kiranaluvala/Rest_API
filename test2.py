from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 5.99},
    {"id": 3, "name": "Product 3", "price": 15.99},
]


# Endpoint to retrieve all products
@app.route('/prod', methods=['GET'])
def get_products():
    return products, 200


# Endpoint to retrieve a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id): 
    try:

        product = next((p for p in products if p["id"] == product_id))
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"message": "Product not found"}), 404
        
    except Exception:
        return {"server not working"}, 500



# Endpoint to create a new product
@app.route('/products/insert', methods=['POST'])
def create_product():
    try:
        new_products = []
        for product in request.json:
            new_product = {
                "id": len(products) + 1,
                "name": product['name'],
                "price": product['price']
            }
            products.append(new_product)
            new_products.append(new_product)
            return jsonify(new_products), 201
        else:
            return jsonify({"message": "Product not found"}), 404
    
    except Exception as e:
        print(e)



# Endpoint to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product["name"] = request.json.get('name', product["name"])
        product["price"] = request.json.get('price', product["price"])
        return jsonify(product), 201
    else:
        return jsonify({"message": "Product not found"}), 404



# Endpoint to delete an existing product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        products.remove(product)
        return jsonify({"message": "Product deleted"})
    else:
        return jsonify({"message": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
