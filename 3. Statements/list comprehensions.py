# when using a for loop using append, list comprehesions can be an alternative
something = "Hello world."
the_list = []  # create empty list

for letter in something: # for every character in 'something'
    the_list.append(letter)  # append every character into the_list
print(the_list)

# to use list comprehension
new_list = [letter for letter in something]
print(new_list)
list_a = [whateveryouwant for whateveryouwant in "This is list comprehension in python."]
print(list_a)
num_list = [nums**3 for nums in range(0, 5)]  # to the power of 3
print(num_list)
new_list = [nums for nums in range(0, 101) if nums % 10==0]   # appends new_list in range 0-100 only if divisible by 10
print(new_list)
c = [0, 10, 20, 30]
f = [((9/5)*temp + 32) for temp in c]
print(f)


cel = [0, 10, 20, 30]
far = []
for temp in cel:
    far.append(( (9/5)*temp + 32))
    print("\n" + str(far))

# if else in list comprehensions...they're hard to read

r = [x if x % 2 == 0 else "odd number" for x in range(10,21)]
print(r)

# nested loops in list comprehensions
num_list = []
for num in [1, 2, 3, 4]:  # regular nested loop
    for nums in [100, 200, 300, 400]:
        num_list.append(num*nums)
print(num_list)
# turning above into list comprehensino using nested loops
num_list_2 = [x*y for x in [1, 2, 3, 4] for y in [100, 200, 300, 400]]
print(num_list_2)