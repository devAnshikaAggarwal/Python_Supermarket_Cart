# A function and exception handling based supermarket program to get items data from an API link and display the bill either send it to the email or print it.

import requests
import smtplib
from email.mime.text import MIMEText

API_URL = "http://demo5472131.mockable.io/supermarket_items"

def fetch_items():
    """Fetches the item list from the API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching items: {e}")
        return []

def display_items(items):
    """Displays available items."""
    print("\nAvailable Items:")
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Name", "Price", "Stock"))
    print("-" * 45)
    for item in items:
        print(f"{item['id']:<5} {item['name']:<15} ${item['price']:<10} {item['quantity']}")

def get_user_selection(items):
    """Lets user select items and returns a cart."""
    cart = []
    while True:
        try:
            item_id = input("\nEnter Item ID to add to cart (or 'done' to finish): ")
            if item_id.lower() == "done":
                break
            item_id = int(item_id)
            item = next((i for i in items if i["id"] == item_id), None)
            if not item:
                print("Invalid item ID. Try again.")
                continue
            quantity = int(input(f"Enter quantity for {item['name']}: "))
            if quantity > item["quantity"]:
                print("Not enough stock available!")
                continue
            cart.append({"name": item["name"], "price": item["price"], "quantity": quantity})
        except ValueError:
            print("Invalid input. Please enter a number.")
    return cart

def calculate_bill(cart):
    """Calculates and prints the bill."""
    total = sum(item["price"] * item["quantity"] for item in cart)
    print("\nYour Bill:")
    print("{:<15} {:<10} {:<10}".format("Item", "Qty", "Subtotal"))
    print("-" * 40)
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        print(f"{item['name']:<15} {item['quantity']:<10} ${subtotal:<10.2f}")
    print("-" * 40)
    print(f"Total Bill: ${total:.2f}")
    return total

def send_email(cart, total, recipient_email):
    """Sends the bill via email."""
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"

    message = "Your Bill:\n\n"
    for item in cart:
        message += f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}\n"
    message += f"\nTotal: ${total:.2f}"

    msg = MIMEText(message)
    msg["Subject"] = "Your Supermarket Bill"
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your-email@example.com", "your-email-password")
            server.sendmail("your-email@example.com", recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main Program Execution
items = fetch_items()
if items:
    display_items(items)
    cart = get_user_selection(items)
    if cart:
        total = calculate_bill(cart)
        choice = input("\nWould you like to (1) Print the bill or (2) Email it? ")
        if choice == "2":
            recipient_email = input("Enter recipient email: ")
            send_email(cart, total, recipient_email)
        else:
            print("Bill printed successfully!")
    else:
        print("No items selected. Exiting.")
else:
    print("Failed to load item data. Please try again later.")
