test_file = open("TEST.txt")  # sets open the test.txt to test_file
print(test_file.read())
print(test_file.read())  # won't print/read twice
test_file.seek(0)  # resets cursor to be able to print again
print(test_file.read())
test_file.seek(0)
print(test_file.readlines())  # outputs a list of contents by line
test_file.close()


# open files by path and append
with open("C:\\Users\\usrname\\xxx\\xxx\\Object and Data Strucure basics\\1. Python Objects and Data Structures\\Files\\TEST.txt", mode='a') as testfile:
    contents = testfile
    print(contents.write("This line was appended."))
# create new file in current path and write to it.n.
with open("this is a new file", mode='w') as n:
    n.write("This file is created.")

