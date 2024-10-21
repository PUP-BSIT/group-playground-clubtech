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
    

            
        
        


        
    
    