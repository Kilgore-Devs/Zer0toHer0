# the range funtion
mylist = [1, 2, 3, 4, 5]
for i in range(0, 11, 2):
    print(i)
nums = list(range(0, 11, 2))  # generates a list using range, more efficient
print(nums)

index_count = 0
for letter in "abcdefg":
    print("At index {} the letter is {}.".format(index_count, letter))
    index_count += 1

new_index = 0  # index count starting at 0
variable = "WORDS"  # string

for l in variable:  # for every char in the vairbale, print index val loc
    print(variable[new_index])
    new_index += 1  # running index count

# same thing but using enumerate
new_variable = "WORDS"  # string

for item in enumerate(new_variable):  # for every char in the vairbale, print index val loc
    print(item)  # get tuples of the index count
for x, y in enumerate(new_variable):
    print(x)    # print coupling line by line with spaces using \n
    print(y)
    print("\n")


# zip is kinda of opposite of enumerate. can use tuple upacking (x, y, etc)
list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]
list_3 = ["A", "B", "C", "D", "E"]
print(list(zip(list_1, list_2, list_3)))
for item in zip(list_1, list_2, list_3):  # zip together as far as shortest list
    print(item)

# in checks if in
something = "a, b, c"
something_else = [1, 2, 3]
print("x" in something)
print(1 in something_else)

print(4 in [1, 2, 3])
print("x" in "x, y, z")
print("Hi" in "Hi, how are you")
print("key" in {"key": 123})

d = {"key1": "value1"}
print( "value1" in d.values())
print( "value1" in d.keys())

the_list = [1, 2, 3, 4, 5, 6, 888, 777]
print(max(the_list))

from random import shuffle
shuffle(the_list)
print(the_list)
from random import randint
i = randint(0,500)
j = i * 4
print(j)
answer = input("What was 4 multiplied by to get " + str(j) + " ?    ")
if answer == i:
    print("Good job!")

else:
    print("Try again")