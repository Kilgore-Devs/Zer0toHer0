make_model = [("Ford", "F150"), ("Ram", "1500"), ("Chevy", "Silverado")]
for vehicle in make_model:
    print(vehicle)
# tuple unpacking
for make, model in make_model:
    print(model)

for make, model in make_model:
    print(make)

make_avg_price = [("Ford", 30000), ("Ram", 40000), ("Chevy", 50000)]
# which make is highest amount
def highest_price(make_avg_price):
    price = 0
    highest = ""

    for make, cost in make_avg_price:
        if cost > price:  # if y or 30000 is greater than cost then
            price = cost  # price becomes y - or "30000" and so on
            highest = make  # highest becomes x - or 'Ford' and so on
        else:
            pass  # if not, pass and continue

    return (highest, price)

highest_price(make_avg_price)  # returns tuple
print(highest_price(make_avg_price))
result = highest_price(make_avg_price)