def myfunc(x):  # defines myfunc and takes in x

    if x == True:  # print and return if true
        print("I like Python.")
        return "I like Python."

    elif x == False:  # print and return if false
        print("I do not like Python. :(")
        return "I do not like Python. :("


y = input("True or False:\nPython is amazing?  ")  # sets x using input
if y == "True" or "true":
    x = True
elif y == "False" or "false":
    x = False
else:
    print("Please try again.")
myfunc(x)  # runs function using the result of if statement
