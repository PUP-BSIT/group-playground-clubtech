 # TODO(John Matthew Arroyo): create a function that will let the customer input the order details
 # TODO(Franco Lazaro): create a function that will calculate for the grand total (including the discount)
 # TODO(John Carlo Nolluda): create a function that will get customer details
 # TODO(Arroyo-Nolluda-Lazaro): create a function that will display the receipt

def get_order():
    orders = []
    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        orders.append ([product_name, price, quantity])
        
        user_confirm = input("Do you want to add another item? (yes-y/no-n): ").lower()
        
        
        print(" ")
        
        if user_confirm != "y":
            break
    
    return orders

def customer_details():
    customer_name = input("Enter your name: ")
    senior_id = int(input("Enter your senior id: "))
    
    return customer_name, senior_id

def total_price(orders, senior_id):
    grand_total = 0        
    for total in orders: 
        total_price = orders[1] * orders[2]
        grand_total += total_price 
        
        if senior_id: 
            grand_total *= 0.9 

    return grand_total
    
def display(orders, customer_name, senior_id, grand_total):
    for item in orders:
        print(f"PRODUCT: {orders[0]}    PRICE: {orders[1] * orders[2]}\n")      
    
    print(f"Customer Name: {customer_name}\n")
        
    if senior_id:
        print(f"SENIOR DISCOUNT APPLIED     Senior Id: {senior_id}\n")
    else:
        print("SENIOR DISCOUNT NOT APPLIED\n")
        
    print(f"Grand Total:    {grand_total}")
    
    
order = get_order()
name, senior = customer_details()
price = total_price(order, senior)
display_all = display(order, name, senior, price)


        
    
    