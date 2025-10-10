
item_0 = {
    "name": "Luke Zheng's shirt",
    "price": "$9.99",
    "category": "Clothing",
    "stock": "One"
}

item_1 = {
    "name": "Johnny Yuan's shoes",
    "price": "$69.99",
    "category": "Clothing",
    "stock": "Two"
}  

item_2 = {
    "name": "Andrew Lee's hair",
    "price": "14.99",
    "category": "Costumes",
    "stock": "One"
}

item_3 = {
    "name": "Ryan Chen's backpack",
    "price": "$44.99",
    "category": "Bags",
    "stock": "One"
}

item_4 = {
    "name": "41-inch longsword",
    "price": "$149.99",
    "category": "Weapons",
    "stock": "Twelve"
}

item_5 = {
    "name": "EasternBlueJay",
    "price": "$1.99",
    "category": "Discord username", 
    "stock": "One"
}

input("What item are you looking for? ") 

if input("0"):
    print(item_0)
elif input("1"):
    print(item_1)
elif input("2"):
    print(item_2)
elif input("3"):
    print(item_3)
elif input("4"):
    print(item_4)
elif input("5"):
    print(item_5)
else:
    print("Sorry, but we do not have the item you are looking for.")