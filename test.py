import json
price_quantity = [{"Name" : "Computer", "Price" : 500, "quantity" : 10},{"Name" : "Monitor", "Price" : 200, "quantity" : 10},{"Name" : "Keyboard", "Price" : 500, "quantity" : 10},{"Name" : "Mouse", "Price" : 10, "quantity" : 10},{"Name" : "Hdmi cable", "Price" : 20, "quantity" : 10},{"Name" : "DVD Drive", "Price" : 50, "quantity" : 10}]
for x in price_quantity:
    if x["Name"] == "Mouse":
        print(x)
print("Welcome to Hehey digital store!")
print("Here is our product's list, feel free to choose and add to your casket! To add item to your casket, please enter the our product's name..")
print(json.dumps(price_quantity,indent=4))
status = "YES"
list_of_product = []
while status == "YES":
    ans = input("What item? ")
    count = int(input("How many? "))
    for product in price_quantity:
        if product["Name"] == ans:
            list_of_product.append(product["Price"]*count)
    cond = input("Do you want to continue add items?").upper()
    if cond == "NO":
        break
total = 0
for nominal in list_of_product:
    total+=nominal
print("Total : ", total)
    
