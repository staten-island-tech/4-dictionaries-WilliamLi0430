items = [
    {   
        "name": "Luke Zheng's shirt",
        "price": "9.99",
        "category": "Clothing",
        "stock": "One"
    },
    {
        "name": "Johnny Yuan's shoes",
        "price": "69.99",
        "category": "Clothing",
        "stock": "Two"
    }, 
    {
        "name": "Andrew Lee's hair",
        "price": "14.99",
        "category": "Costumes",
        "stock": "One"
    },
    {
        "name": "Ryan Chen's backpack",
        "price": "44.99",
        "category": "Bags",
        "stock": "One"
    },
    {
        "name": "41-inch longsword",
        "price": "149.99",
        "category": "Weapons",
        "stock": "Twelve"
    },
    {
        "name": "EasternBlueJay",
        "price": "1.99",
        "category": "Discord username", 
        "stock": "One"
    },
    {
        "name": "Github Desktop",
        "price": "5000",
        "category": "Online Services",
        "stock": "Ten Thousand"
    },
    {
        "name": "Tencent",
        "price": "722000000000",
        "category": "Gaming",
        "stock": "One"
    }
]

cart = []
cost = 0
e = 1
while e == 1:
    for index, item in enumerate(items):
        print(index, ":", item["name"])
    a = int(input("What item(s) do you want to buy? (0-7) "))
    cart.append(items[a]["price"])
    cart.append(items[a]["name"])
    cost += (float(items[a]["price"]))
    rounding = round(cost, 3)
    b = input("Do you wish to continue? ")
    if b == ("yes") or b == ("Yes"):
        e += 0
    else:
        print(cart)
        t = input("Are you sure you want to buy these items? ")
        if t == ("yes") or t == ("Yes"):
            print(f"Your total is ${rounding}")
            break
        else:
            print(cart)
            dumb = input("Which item do you want to remove?")
            cart.remove(dumb("name"))
            cart.remove(dumb("price"))
            print(cart)