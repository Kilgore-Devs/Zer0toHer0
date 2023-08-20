# sets have unordered and unique elements
# this means there can only be one representative of the same object
this_set = set()
print(this_set)
this_set.add(1)
print(this_set)
this_set.add(2)
print(this_set)
# try to add 1 again but doesn't, it has to be unique
this_set.add(1)
print(this_set)
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
print(nums)
print(set(nums))  # turns list into set and displays, can and prolly will be unordered
print(set([1,1,2,3]))

