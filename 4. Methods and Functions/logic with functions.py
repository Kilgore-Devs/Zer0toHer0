# using functions with logi
# check if a number is odd
def odd_checker(num):
    result = num %2 != 0
    print(f"The result of the number being odd is: {result}") # this will show if True of False
    return  result


odd_checker(21)
odd_checker(20)

# retuen True if any number in list is false

def check_odd_list(numbers_list):
    odd_numbers = []  # creates an empty list to fill
    for number in numbers_list:
        if number % 2 != 0:
            odd_numbers.append(number)  # appends odd numbers to empty list

        else:
            pass
    return odd_numbers  #  placed outside if statement to esnure the entirity of list is looped through


check_odd_list([3, 5, 7, 8])
print(check_odd_list([3, 5, 7, 8])) # print the result of the function

