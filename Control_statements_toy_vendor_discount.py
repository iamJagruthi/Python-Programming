# Toy Vendor Discount Program
def calculate_discounted_price(product_code, order_amount):
    if product_code == 1:  # Battery Based Toys
        if order_amount > 1000:
            discount = order_amount * 0.10  # 10% discount
        else:
            discount = 0
    elif product_code == 2:  # Key-Based Toys
        if order_amount > 100:
            discount = order_amount * 0.05  # 5% discount
        else:
            discount = 0
    elif product_code == 3:  # Electrical Charging Based Toys
        if order_amount > 500:
            discount = order_amount * 0.10  # 10% discount
        else:
            discount = 0
    else:
        print("Invalid product code.")
        return None

    net_amount = order_amount - discount
    return net_amount

# Input for toy vendor program
product_code = int(input("Enter product code (1: Battery, 2: Key-based, 3: Electrical Charging): "))
order_amount = float(input("Enter the order amount (Rs.): "))
net_amount = calculate_discounted_price(product_code, order_amount)

if net_amount is not None:
    print("Net amount after discount: Rs.", net_amount)
