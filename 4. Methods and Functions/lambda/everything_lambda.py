def square(n):
    return n**2


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = reversed(nums)  # reverses order of "nums"
map(square, nums)  # pass in function you want to map to every item in list
print(map(square, nums))  # prints memory location
""" To iterate the function through the list, 
need to use a for loop"""
for item in map(square, nums2):
    print(item)

for item in map(square, nums):
    print(item)

print(list(map(square, nums)))  # maps square to items in nums, prints as a list


def splicer(words):
    if len(words) % 2 == 0:  # if len of 'words' is even
        return "Even"  # return even else return first letter
    else:
        return words[0]


cars = "M3", "Accord", "Viper", "Challenger"

print(list(map(splicer, cars)))  # dont add () after fx name, it's an arg,  not calling the fx


def check_even(number):
    return number % 2 == 0


thenums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter(check_even, thenums))

for n in filter(check_even, thenums):
    print(n)

print(list(filter(check_even, thenums)))
# lambda uses
square  = lambda n: n ** 2  # converting square fx into lambda
print(square(99))

print(list(map(lambda num: num**2, nums)))
print(list(filter(lambda num: num % 2 == 0, thenums)))  # checks for even numbers in thenums list

print(list(map(lambda names: names[0], cars)))  # prints first letter of each item in cars list, via filtering
print(list(map(lambda names: names[::-1], cars)))  # reverses
