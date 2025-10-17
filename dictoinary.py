items = [
    {   
        "name": "Luke Zheng's shirt",
        "price": "$9.99",
        "category": "Clothing",
        "stock": "One"
    },
    {
        "name": "Johnny Yuan's shoes",
        "price": "$69.99",
        "category": "Clothing",
        "stock": "Two"
    }, 
    {
        "name": "Andrew Lee's hair",
        "price": "$14.99",
        "category": "Costumes",
        "stock": "One"
    },
    {
        "name": "Ryan Chen's backpack",
        "price": "$44.99",
        "category": "Bags",
        "stock": "One"
    },
    {
        "name": "41-inch longsword",
        "price": "$149.99",
        "category": "Weapons",
        "stock": "Twelve"
    },
    {
        "name": "EasternBlueJay",
        "price": "$1.99",
        "category": "Discord username", 
        "stock": "One"
    },
    {
        "name": "Github Desktop",
        "price": "$5,000",
        "category": "Online Services",
        "stock": "Ten Thousand"
    },
    {
        "name": "Tencent",
        "price": "$722.39 billion",
        "category": "Gaming",
        "stock": "One"
    }
]

for index, item in enumerate(items):
    print(index, ":", item["name"])
a = int(input("What item(s) do you want to buy? (0-7) "))
print (items[a])