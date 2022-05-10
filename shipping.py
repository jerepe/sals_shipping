# Defining main variables:
weight = float(input("Please enter the weight: "))
shipping_method = int(input("""
Which shipping method do you want to chose? (Type in the number only)

1 - Ground_Shipping
2 - Ground_Shipping_Premium
3 - Drone_Shipping

Shipping choice: """))


# Ground shipping cost generation:
if shipping_method == 1 and weight <= 2:
    cost_ground = (weight * 1.5) + 20
if shipping_method == 1 and weight > 2 and weight <= 6:
    cost_ground = (weight * 3) + 20
elif shipping_method == 1 and weight > 6 and weight <= 10:
    cost_ground = (weight * 4) + 20
else:
    cost_ground = (weight * 4.75) + 20

# Premium ground shipping cost generation:
cost_premium = 125.00

# Drone shipping cost generation:
if shipping_method == 3 and weight <= 2:    
    cost_drone = (weight * 4.50)
elif shipping_method == 3 and weight > 2 and weight <= 6:
    cost_drone = (weight * 9.00)
elif shipping_method == 3 and weight > 6 and weight <= 10:
    cost_drone = (weight * 12.00)
else:
    cost_drone = (weight * 14.25)

# total cost printing using user choice of delivery:
if shipping_method == 1:
    print("Total cost is: $" + str(cost_ground))
    print("Note: Premium Ground Shipping costs $" + str(cost_premium))
elif shipping_method == 2:
    print("Total cost is: $125.00")
elif shipping_method == 3:
    print("Total cost is: $" + str(cost_drone))
    print("Note: Drone Shipping costs $" + str(cost_drone))
else:
    print("Error ... please try again")
