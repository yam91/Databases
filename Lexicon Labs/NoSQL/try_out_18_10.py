from functools import reduce 

product1 = {
    "name" : "saucepan",
    "price" : 30,
    "category" : "kitchen",
    "stock quantity": 200,
    "customer reviews": ["Heat does not distribute uniformly."]
}

product2 = {
    "name" : "4-set plates",
    "price" : 100,
    "category" : "kitchen",
    "stock quantity": 500,
    "customer reviews": ["Beautiful plates. I love them!"]
}

order1 = {
    "products" : [product1, product2],
    "total amount" : 0,
    "status": "pending"
}

order1["total amount"] = sum([x["price"] for x in order1["products"]])

