def myfunc(u):  # defines myfunc and takes in x

    if x == True:  # print and return if true
        print("I like Python.")
        return "I like Python."

    elif x == False:  # print and return if false
        print("I do not like Python. :(")
        return "I do not like Python. :("


y = input("True or False:\nPython is amazing?  ")  # sets x using input
y = y.capitalize()  # make users input of true or false start with capital letter
if y == "True":  # if y is True then x is True
    x = True

elif y == "False":  # If y is False then x is False.
    x = False

else:
    print("Please try again.")


myfunc(x)  # runs function using the result of if statement
