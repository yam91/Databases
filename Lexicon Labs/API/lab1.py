import requests
import json

'''
url = "https://api.github.com/users/yam91/repos"

response = requests.get(url)
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo['name'])
else :
    print(f"Unable to retrieve repositories.\nError {response.status_code} occurred.")
'''

menu = {1: 'Show all products', 2: 'Show product details', 3: 'Add a product', 4: 'Quit'}

def show_all_prodcuts ():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f'{product}\n')
    else:
        print(f"Unable to retrieve the list of products.\nError {response.status_code} occurred.")
        exit


def show_product():
    product_num = int(input("Which product do you want to see? Enter product number: "))
    url = f"https://fakestoreapi.com/products/{product_num}"
    response = requests.get(url)
    if response.status_code == 200:
        product = response.json()
        print(f'{product}\n')
    else:
        print(f"Unable to retrieve the product.\nError {response.status_code} occurred.")
        exit

def add_product():
    url = f"https://fakestoreapi.com/products"
    print("Enter the following deatils on the product you wish to insert:\n")
    new_product_dict = {'title' : input("title: "), 'price' : float(input("price: ")), 'description' : input("description: "),\
                        'image' : input("url of an image: "), 'category' : input("category: ")}
    new_product = json.dumps(new_product_dict)
    print(new_product)
    response = requests.post(url, new_product)
    if response.status_code == 200:
        product = response.json()
        print(f'{product}\n')

    else:
        print(f"Unable to add the product.\nError {response.status_code} occurred.")
        exit

def optionsHandler(user_input):
    if user_input == 1:
        show_all_prodcuts()
        
        print(f'Choose a number from \n{menu}')
        optionsHandler(int(input()))
           
    if user_input == 2:
        show_product()

        print(f'Choose a number from \n{menu}')
        optionsHandler(int(input()))

    if user_input == 3:
        add_product()

        print(f'Choose a number from \n{menu}')
        optionsHandler(int(input()))

    if user_input == 4:
        exit

def main():
    print(f'Choose a number from \n{menu}')
    user_input = int(input())
    optionsHandler(user_input)

main()