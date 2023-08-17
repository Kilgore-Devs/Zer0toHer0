# strings are immutable
name = "Dad"  # cant change Dad to Sad
# name[0] = "S" throws error
new_name = name[1:]
print(new_name)
print("S" + new_name)

x = "Hello World"
print(x + ", it's nice to meet you!")
x = x + ", it's nice to meet you!"  # reassign x
print(x)
y = "Zz"
print(y * 5)  # multuplies Zz by 10 and prints
print(y.upper())  # prints y in upper. can use .lower()
a = "This is Python"
print(a.split())

print(a.split("t"))  # splits at "t"

