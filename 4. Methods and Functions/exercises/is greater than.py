def is_greater(x, y):
    if x > y:
        print(f"{x} is greater than {y}")
        return True
    else:
        print(f"{x} is less than or equal {y}")
        return False


x = float(input("Input a random number   "))
y = float(input("\nInput a random number   "))
is_greater(x, y)
