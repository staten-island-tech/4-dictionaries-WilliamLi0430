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
    },
    {
        "name": "Nothing",
        "price": "0",
        "category": "For nothing",
        "stock": "Infinite"
    }
]

cart = []
money = []
cost = 0
while True: 
    for index, item in enumerate(items):
        print(index, ":", item["name"])
    a = int(input("What item(s) do you want to buy? (0-8) "))
    if a > 10  or a < 0:
        print("Invalid item")
    money.append(items[a]["price"])
    cart.append(items[a]["name"])
    cost += (float(items[a]["price"]))
    rounding = round(cost, 3)
    print(cart)
    b = input("Do you wish to continue? ")
    if b == ("yes") or b == ("Yes"):
        print(f"Your current total is ${rounding}")
    else:
        print(cart)
        t = input("Are you sure you want to buy these items? ")
        if t == ("yes") or t == ("Yes"):
            print(f"Your total is ${rounding}")
            break
        else:
            while True:                
                print(cart)
                dumb = int(input("Which item do you want to remove? "))
                del cart[dumb]
                del money[dumb]
                print(cart)
                ask = input("Do you wish to continue removing items? ")
                if ask == ("Yes") or ("yes"):
                    print("Returning to remove screen:")
                #fix this part
                elif ask == ("No") or ("no"):
                    print("Going back to the shop...")
                    break
                else:
                    print("Invalid")