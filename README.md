# Supermarket Billing System

This is a Python-based supermarket billing program that fetches item data from an API, allows users to select items, calculates the total bill, and provides an option to either print the bill or send it via email.

## Features
- **Fetch Items from API**: Retrieves available supermarket items (name, price, stock quantity) from an external API.
- **Display Items**: Shows a formatted list of available products with prices and stock.
- **User Selection**: Allows users to add items to the cart by specifying item ID and quantity.
- **Bill Calculation**: Computes the total cost of the selected items.
- **Print or Email Bill**: Users can either print the bill or send it to an email address.
- **Error Handling**: Handles invalid inputs, stock limitations, and API failures gracefully.

## How to Run
1. Ensure you have Python installed (Python 3.x recommended).
2. Install required dependencies (if not already available):
   ```sh
   pip install requests smtplib email
   ```
3. Run the script:
   ```sh
   python supermarket_billing.py
   ```
4. Follow on-screen prompts to select items and generate a bill.

## Example Output
```
Available Items:
ID    Name            Price     Stock    
----------------------------------------
1     Apple          $2.00     50       
2     Banana         $1.50     30       
3     Milk          $3.00      20       
...

Enter Item ID to add to cart (or 'done' to finish): 1
Enter quantity for Apple: 2
...

Your Bill:
Item            Qty        Subtotal    
----------------------------------------
Apple           2         $4.00       
...
----------------------------------------
Total Bill: $10.50

Would you like to (1) Print the bill or (2) Email it?
```

## Configuration
- Update `API_URL` with the correct API endpoint for fetching supermarket items.
- Configure SMTP settings for sending emails securely (App Passwords recommended).

## Requirements
- **Python 3.x**
- **Internet connection** (for API and email services)
- **Gmail SMTP access** (or alternative email provider settings)
