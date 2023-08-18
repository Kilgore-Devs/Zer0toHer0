# .format()
# "The {} is {} like this".format("string", "formatted")
print("This is a string is {}!".format("FORMATTED"))
print("The {} {} {}".format("dog", "ate", "food"))
print("The {2} {1} {0}".format("dog", "ate", "food"))  # can index: 2=dog, 1=ate, 0=food
print("The {a} {b} {c}".format(a= "dog", b= "ate", c= "food"))

# float formatting with percision
answer = 200/88
print(answer)
print("The result is {r:1.3f}:".format(r= answer))  #format flaots with value:width/whitespace, perison f
#string literal method skips .format() method
name = "Me"
print(f"Hello {name}")  # 'f' before string then variable in the {}



