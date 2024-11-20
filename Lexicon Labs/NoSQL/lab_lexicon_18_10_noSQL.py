'''
You are going to create a system to manage the inventory of an online e-commerce store, with products, categories, orders, and customer data.
 
Collections:
-Name the database ecommerce store.
-Store product details like name, price, category, stock quantity, and a list of customer reviews.
-Store categories with attributes like category name, description, and a list of products in that category.
-Store customer information like name, address, and their order history.
-Store details of customer orders including customer ID, products purchased, total amount, and the status of the order (pending, shipped, etc.).
 
Insert data:
-Add product data with various categories (e.g., electronics, clothing, etc.).
-Add customer data with initial information.
-Insert some orders where customers have purchased multiple products.
 
Good luck! 
'''

from pymongo import MongoClient 

# 1. set-up the library db and collections: books, authors and users
client = MongoClient('mongodb://localhost:27017')
db = client['ecommerce']

# products collection:
products = db['products']
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

product3 = {
    "name" : "Bose noise-cancelling headphones",
    "price" : 300,
    "category" : "electronics",
    "stock quantity": 150,
    "customer reviews": ["I returned them because the noise cancelling gave me a headache. :("]
}

product4 = {
    "name" : "Iphone5",
    "price" : 1000,
    "category" : "electronics",
    "stock quantity": 50,
    "customer reviews": ["The camera is amazing!"]
}

product5 = {
    "name" : "Levi's jeans",
    "price" : 50,
    "category" : "clothing",
    "stock quantity": 100,
    "customer reviews": ["So comfy!"]
}

products.insert_many([product1, product2, product3, product4, product5])

# categories collection:
categories = db['categories']
category1 = {
    "name" : "kitchen",
    "description" : "various kitchen utensils",
    "products" : [product1]
}

category2 = {
    "name" : "clothing",
    "description" : "clothes for men and women",
    "products" : [product5]
}

category3 = {
    "name" : "electronics",
    "description" : "anything that can connect to a socket",
    "products" : [product3, product4]
}

categories.insert_many([category1, category2, category3])

# customers collection:
customers = db['customers']
customer1 = {
    "name" : "Maria Bianco",
    "adress" : "Margaretha Krooks Gata 10, 12654, Hägersten, Stockholm",
    "order history" : [product1, product2, product5]
}

ustomers = db['customers']
customer2 = {
    "name" : "Dan Arieli",
    "adress" : "Drottninggatan 20 11151, Stockholm",
    "order history" : [product3, product4]
}

customers.insert_many([customer1, customer2])

# orders collection:
orders = db['orders']
# after adding customers to collection, can access "_id" key.
order1 = {
    "customerID" : customer1["_id"],
    "products" : [product1, product2],
    "total amount" : 0,
    "status": "shipped"
}

order2 = {
    "customerID" : customer1["_id"],
    "products" : [product5],
    "total amount" : 0,
    "status": "pending"
}

order3 = {
    "customerID" : customer2["_id"],
    "products" : [product3],
    "total amount" : 0,
    "status": "shipped"
}

order4 = {
    "customerID" : customer2["_id"],
    "products" : [product4],
    "total amount" : 0,
    "status": "cancelled"
}

orders.insert_many([order1, order2, order3, order4])

# update price for all inserted orders:
# before update:
all_orders = orders.find()
for order in all_orders:
    print(order)
print("\n\n")
all_orders = orders.find()
for order in all_orders:
    query = {"_id" : order["_id"]}
    #total = sum([x["price"] for x in order["products"]])    
    update_operation = {"$set" : { "total amount" : sum([x["price"] for x in order["products"]]) }}
    orders.update_one(query, update_operation)

# after update:
all_orders = orders.find()
for order in all_orders:
    print(order)
print("\n\n")

# delete cancelled orders
cancelled_query = {"status": "cancelled"}

# show cancelled order
cancelled_orders = orders.find(cancelled_query)
for canc_order in cancelled_orders :
    print(canc_order)

orders.delete_many(cancelled_query)
print("\n\n")

# after delete:
all_orders = orders.find()
for order in all_orders:
    print(order)