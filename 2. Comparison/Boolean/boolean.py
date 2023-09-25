# Boolean are operators that allow you to convey is something is True or False
print(type(False))  # is a boolean
print(type("false"))  # is a string
# check True or False
print(bool(1 > 2))  # checks if true or false
print(bool(1 = 1))  # checks if not equal to
name = None  # place holder for "name" for later use
print(type(name))  # "NoneType"
print(2.0 == 2)  # is equal to?
print(2.0 == "2")
print(2.0 != "2")  # not equal to
# >
# <
# >=
# <=
# Logical operators allow chaining of comparison operators
# and/or/not
print(1 == 1 and 1 == 2)  # both must be true
print(1 == 1 or 1 == 2)  # one must be true
print(not 1 == 1)  # opposite
counter = 0  # set counter
while counter <= 100:  # while counter is less than 100 do the loop
    counter += 1  # increment counter by 1
    print(counter)  # print the counter
