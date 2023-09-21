# since many objects in python are iterable,
# loops can execute a block of code for every iteration
# iterable mean you can perform an action for every 'thing' in
# the object it char in string, items in a list, dict, tuple
my_list = [1, 2, 3]
for item in my_list:  # item is just a place holder for what is being iterated..can choose whatever
    print(item)  # for this example, prints 'item' or whats in the list

car_types = ["sedan", "hatchback", "coupe"]

for cars in car_types:
    print(cars)

numbers = range(1, 21)  # defines numbers = range
# nums = list(numbers)  # if you cannot iterate, can turn into list
for n in numbers:  # iterates through and prints statement for each item in the range
    if n > 1:
        print("This is " + str(n) + " iterations of the list made from a range.")
    else:
        print("This is " + str(n) + " iteration of the list made from a range.")

for n in numbers:
    # check for odds
    if n % 2 > 0:  # even mubers are divisble by 2 with no remainders, so if remainder is greater than 0 then it's odd
        print(str(n) + " is an odd number")
    else:
        print(f"{n} is an even number.")  # using f string formatting

list_total = 0

for n in numbers:
    list_total = list_total + n
    print(list_total)  # if print is inside for loop, it'll show every step
print(list_total)  # if print is outside, it will only show the final number

# for loops with strings

the_string = "Python"

for letter in the_string:  # can call 'letter' whatever you want
    print(letter)
    print("Python")
# using loops with tuples
the_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
for _ in the_tuple:  # can use _ if you don't want to use anything
    print(_)
# tuple unpacking
unpack_me = [(1, 2), (3, 4), (5, 6), (7, 8)]  # a list of tuple pairs
print(len(unpack_me))
for i in unpack_me:
    print(i)
for a, b in unpack_me:  # unpack by making variable separated by comma
    print(a,b)

# iterating through dicts
small_dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
for k in small_dict.items():  # this just gets items, .keys() and .values() to get keys or values
    # above you can use tuple uppacking by k,v
    print(k)
