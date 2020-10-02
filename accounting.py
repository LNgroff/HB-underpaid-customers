melon_cost = 1.00


## creating a function to calculate which customers has underpaid
def order_history('customer-orders.txt'):
    customer_order = open('customer-order.txt')
    #opens the file with orders
    
    #iterate through each line/order in the file
    for line in customer_order:
        order = line.split('|')
        #splits each order into "grabable" pieces, split by '|'

        ord_num = order[0]
        #identifies the line/order by number
        name = order[1]
        #identifies the second item as the customers 'name'
        melon_num = float(order[2])
        #identifies the third item as the number of melons bought 
        paid = float(order[3])
        #identifies fourth item as the amount that the customer paid
        
        expected = melon_num * melon_cost
        #calculates how much the customer should have paid
        
        print(f"{name} paid ${paid:.2f}, they should have paid ${expected:.2f}")
        #prints how much each customer paid and what they should have paid.

        if expected > paid:
            #if they under paid, print the following
            print(f"{name} underpaid.")
        elif expected < paid:
           #if they over paid, print the following.
            print(f"{name} overpaid.")

    customer_order.close()

order_history("customer-orders.txt")

'''
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00



customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
'''