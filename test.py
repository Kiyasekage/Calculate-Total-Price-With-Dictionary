import json
price_quantity = [{"Name" : "Computer", "Price" : 500, "quantity" : 10},{"Name" : "Monitor", "Price" : 200, "quantity" : 10},{"Name" : "Keyboard", "Price" : 500, "quantity" : 10},{"Name" : "Mouse", "Price" : 10, "quantity" : 10},{"Name" : "Hdmi cable", "Price" : 20, "quantity" : 10},{"Name" : "DVD Drive", "Price" : 50, "quantity" : 10}]
print("Welcome to Hehey digital store!")
print("Here is our product's list, feel free to choose and add to your casket!")
print(json.dumps(price_quantity,indent=4))
status = "YES"
while status == "YES":
    ans = input("")
    cond = input("Do you want to continue add items?").upper()
    if cond == "YES":
        break
