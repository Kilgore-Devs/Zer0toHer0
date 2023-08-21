# While loops continues to exe block of code while condition is true
# while bool_condition:
#   do something
# else
#   do something different

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x = x + 1  # adds 1 to x. can use x += 1
else:
    print(" x is no longer less than 5.")

x = [10, 11, 12]
for _ in x:
    pass  # do nothing at all
y = " Melanie"
for l in y:
    if l == "M":  # if letter is M, go back to beginning of loop, skips M
        continue
    print(l)
for n in y:
    if n == "e":
        break  # breaks out of curent closest loop, so prints M and stops
    print(n)

a = 0  # sets a to 0
while a < 10: # while a is less than 10, runt the block of code
    if a == 5:  # if a is eqaul to 5, break out/stop
        break
    print(a)  # prints a + 1
    a += 1