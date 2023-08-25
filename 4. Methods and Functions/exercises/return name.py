"""Function that takes in a name and prints Hello. have a good day"""


def myfunc(name):
    # returns Hello {}. format(name) and make first letter of name capitalized
    print('Hello {}. \nHave a great day!!'.format(name.capitalize()))


name = input("What is your name?  ")

myfunc(name)
