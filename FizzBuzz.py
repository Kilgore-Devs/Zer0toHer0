numbers = range(0, 100)
for nums in numbers:
    if nums % 3 ==0 and nums %5==0:
        print("FizzBuzz")
    elif nums %3==0:
        print("Fizz")
    elif nums %5==0:
        print("Buzz")
    else:
        print("Didnt work. " + nums)