best_buy_items = []
item = {
    "name": "Luke Zheng's shirt",
    "price": 3.00,
    "category": "Clothing",
    "stock": "One"
}

item = {
    "name": "Johnny Yuan's shoes",
    "price": 70.00,
    "category": "Clothing",
    "stock": "Two"
}  

item = {
    "name": "Andrew Lee's hair",
    "price": 15.00,
    "category": "Costumes",
    "stock": "One"
}

item = {
    "name": "Ryan Chen's backpack",
    "price": 45.00,
    "category": "Bags",
    "stock": "One"
}


best_buy_items[0]["price"]

for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])