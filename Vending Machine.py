# Menu storing all products: code -> [name, price]
products = {
    "A1": ["Coke", 3.0],
    "A2": ["Pepsi", 3.0],
    "A3": ["Sprite", 3.0],
    "A4": ["Water", 2.0],
    "A5": ["Juice", 4.0],
    "A6": ["Iced Tea", 4.5],
    "A7": ["Coffee", 5.0],
    "A8": ["Strawberry Milk", 3.0],
    "A9": ["Mirinda Citrus", 5.0],
    "B1": ["Lays", 2.5],
    "B2": ["M&Ms", 3.5],
    "B3": ["Cookies", 3.0],
    "B4": ["Skittles", 1.0],
    "B5": ["Mentos", 1.5],
    "B6": ["Sandwich", 10.0]
}

# Display vending machine menu
print("---VENDING MACHINE MENU---")
for code, info in products.items():  # Loop through each product
    print(f"{code} - {info[0]} : {info[1]} SAR")  # This shows the code, name, and price

# Initialize shopping cart and total price
total_price = 0
cart = []

# This is the loop for selecting products
while True:
    code = input("Enter product code: ").strip().upper()  # Get input and standardize it

    if code in products:  # Check if code exists
        item_name = products[code][0]  # Get product name
        item_price = products[code][1]  # Get product price

        cart.append(item_name)  # Add item to cart
        total_price += item_price  # Add price to total

        print(f"Added: {item_name} - {item_price} SAR")  # Confirm addition
    else:
        print("Invalid product code. Try again.")  # Error for puting wrong code
        continue  # Goes back to the start of loop

    # This code asks if user wants to buy another item
    again = input("Do you want to purchase another item? (yes/no): ").strip().lower()
    if again == "no":  # If no, exit the loop
        break

# Displays final cart and the total price of the items
print("Your cart:", cart)
print("Total amount:", total_price, "SAR")

# Payment process
amount = float(input("Please enter the amount to the machine: "))  # Get money from user

# This checks if the inserted amount is enough
if amount > total_price:
    change = amount - total_price  # Calculate change
    print("Thank you for your purchase!")
    print("Your change is:", round(change, 2), "SAR")  # Return change

elif amount == total_price:  # Exact payment
    print("Thank you! Exact amount received.")

else:  # If there is not enough money
    shortage = total_price - amount
    print("Insufficient amount! You are short by:", round(shortage, 2), "SAR")
