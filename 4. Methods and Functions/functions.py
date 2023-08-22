# methods are basically functino built in to objects
mylist = [1, 2, 3]
mylist.append(4)
print(mylist)
mylist.pop()
print(mylist)

help(mylist.insert)  # help function shows 'documentation'

# create a function by using 'def'
# def funtion_name():          # use snake_casing when naming functions
# """optional doc string to describe the function"""
#   print("Hello")   # function prints Hello. needs to be indented a denoted by the ':' in the def line
def print_hi():
    """This function prints 'hi'"""
    print("hi")
print_hi()


def print_hi_name(name):  # accepts parameter or arg
    print("Hi" + name)

print_hi_name(" Brandon")


def add_function(num1, num2):
    """Create a function that takes 2 var/arg and returns arg1+arg2."""
    return num1+num2  # Return allows result to be saved to a variable.

answer = add_function(10,2)
print(answer)

print_hi()  # can call function whenever

def print_hi_name(name = input("What is your name?  ")):  # assigning defaul value for name
    print(f'Hello {name}')

print_hi_name()

def minus_calc(number1, number2):
    return(number1-number2)
    

minus_calc(10,12)
result = minus_calc(10,12)
print(result)


