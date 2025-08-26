# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${final_price:.2f}")
