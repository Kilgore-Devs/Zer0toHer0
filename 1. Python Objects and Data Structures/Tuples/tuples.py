# Tuples are similar to lists, cannot be changed or mutated
# inside parenthesis ()
# tuples can have a list inside: tuple = (1, 2, [3, 4])
t = (1, 2, 3, 4, 5, 5)
l = [1, 2, 3, 4, 5]
print(type(t))
print(type(l))
print(t[5])
print(t.count(5))  # counts how many times something is in a tuple
print(t.index(5))  # index loc of where 5 is
# you can reassign in lists but not in tuples
l[0] = 0  # change index 0 to 0
print(l)
