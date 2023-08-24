make_model = [("Ford", "F150"), ("Ram", "1500"), ("Chevy", "Silverado")]
for vehicle in make_model:
    print(vehicle)
# tuple unpacking
for make, model in make_model:
    print(model)

for make, model in make_model:
    print(make)

make_avg_price = [("Ford", 30000), ("Ram", 40000), ("Chevy", 60000)]
# which make is highest amount
def highest_price(make_avg_price):
    msrp = 0
    highest_cost = ""

    for make, cost in make_avg_price:
        if cost > msrp:  # if y or 30000 is greater than cost then
            msrp = cost  # price becomes y - or "30000" and so on
            highest_cost = make  # highest becomes x - or 'Ford' and so on
        else:
            pass  # if not, pass and continue

    return (highest_cost, msrp)

highest_price(make_avg_price)  # returns tuple
print(highest_price(make_avg_price))  # prints output of function
result = highest_price(make_avg_price)
print(result)
vehicle_make, vehicle_price = highest_price(make_avg_price)  # tuple unpacking with function call
print(vehicle_make)  # printing the tuple unpacking
print(vehicle_price)
# test what items are in a tuple of any function


