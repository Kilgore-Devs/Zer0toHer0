# lists are ordered and in []. Retrieved by location.
the_list = [10, 9, 8]  # cant be any combo of data type ie boolean, float, string.
print(len(the_list))
print(the_list[0:3])  # slice and index the same way as a string
next_list = [7, 6, 5]
print(the_list + next_list)  # can concatenate
# can change list
next_list[2] = 4  # changes index 2 to 4
print(next_list)
next_list.append(5)  # adds '5' at the end of list, can add anything
print(next_list)
next_list.pop(2)
print(next_list)
popped_item = next_list.pop(2)  # saves popped item from the .pop() above
print(popped_item)

mylist = ["a", "g", "r", "e", "x", "u"]
nums = [1, 3, 7, 8, 5, 4, 9]
mylist.sort()  # sorts list
print(mylist)  # prints called sorted list. cannot reassign sort ist. it will = NoneType
nums.sort()
print(nums)
nums.reverse()
print(nums)  # reverses the sort