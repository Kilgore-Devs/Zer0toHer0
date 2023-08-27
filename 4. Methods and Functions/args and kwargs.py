def myfunc(a,b,c,d,e=0):
    # Returns 5% of sum of a and b
    return sum((a, b,c , d, e)) * .05

myfunc(100, 100, 100, 100)
print(myfunc(100, 100, 100, 100))  # print to see the result...as a demo

def newfunc(*arg):  # *'args' can be whatever
    # unlimited args. (as a tuple)
    return  sum(arg) * 0.05

print(newfunc(10,10,10,10,10,10,345320,340,320,30,90))

def func3(**kwargs):  # keywords as an argument as a dictionary
    print(kwargs)  # prints kwargs that are passed in
    if 'fruit' in kwargs:
        print("My favorite fruit is {}.".format(kwargs["fruit"]))
    else:
        print("Theres no fruit.")

func3(fruit="apple", veggie="tomato")

def func4(*args, **kwargs):
    print(args) # prints args and kwargs to so inputs
    print(kwargs)
    print("I would like {} {} for dinner.".format(args[2], kwargs["food"]))

func4(5, 6, 7, food = "pizzas", side = "fries", dessert = "icecream" )