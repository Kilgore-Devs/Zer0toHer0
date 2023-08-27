# Function to find the a percentage of the sum of two numbers

n = float(input("What percentage do you want to find?  "))
p = float(n/100)


def myfunc(a, b):
    # Returns 5% of sum of a and b
    return sum((a, b)) * p


z = n
x = float(input("Let's find " + str(z) + "% of the sum of two numbers. \nWhat should the first number be?   "))
y = float(input("And the second?   "))
myfunc(x, y)
print(f"{z}% of {x} and {y} equals:")
print(myfunc(x, y))
