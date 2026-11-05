# Calculate-Total-Price-With-Dictionary
A simple Python shopping cart simulation for a digital store. The program displays a list of available products along with their prices and quantities. Users can select products, specify how many they want to purchase, and calculate the total cost of their selected items.

## Features

- **Product Catalog:** Stores product information, including names, prices, and available quantities.
- **Product Search:** Uses a `for` loop and conditional statements to find a specific product.
- **JSON Formatting:** Displays the product catalog in a structured and readable format using `json.dumps()`.
- **Shopping Cart:** Stores the calculated costs of selected products in a list.
- **Quantity Selection:** Allows users to specify the number of items they want to purchase.
- **Multiple Purchases:** Supports adding multiple products before calculating the total.
- **Total Calculation:** Uses a loop to calculate the final purchase amount.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `digital_store.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python digital_store.py
   ```

5. Browse the available products.
6. Enter the product name and desired quantity.
7. Continue adding products or enter `NO` to finish shopping.
8. View your total purchase cost.

## Example

**Available Products:**

```json
[
    {
        "Name": "Computer",
        "Price": 500,
        "quantity": 10
    },
    {
        "Name": "Monitor",
        "Price": 200,
        "quantity": 10
    },
    {
        "Name": "Keyboard",
        "Price": 500,
        "quantity": 10
    },
    {
        "Name": "Mouse",
        "Price": 10,
        "quantity": 10
    },
    {
        "Name": "Hdmi cable",
        "Price": 20,
        "quantity": 10
    },
    {
        "Name": "DVD Drive",
        "Price": 50,
        "quantity": 10
    }
]
```

**Example Shopping Session:**

```text
Welcome to Hehey digital store!

What item? Computer
How many? 2
Do you want to continue add items? YES

What item? Mouse
How many? 1
Do you want to continue add items? NO

Total : 1010
```

*Note: The prices are example values from the program, without a specified currency.*

## Concepts Practiced

- **Lists:** Storing product information and shopping cart values.
- **Dictionaries:** Representing products through key-value pairs.
- **Loops:** Iterating through products and calculating the total cost.
- **Conditional Statements:** Checking product names and controlling the shopping process.
- **User Input:** Collecting product selections and quantities.
- **JSON:** Formatting product information using `json.dumps()`.
- **Arithmetic Operations:** Multiplying product prices by quantities and calculating the final total.

## Language

Python 3
