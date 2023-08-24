# take output of one function into the input into another
# shuffle list at random
example = [1, 2, 3, 4, 5, 6, 7]
from random import shuffle

def shuff_list(mylist):
    shuffle(mylist)
    return mylist

results = shuff_list(example)  # uses the return resutls of the function and assign to results variable
print(results)  # just used to print the variable


mylist = [" ", "O", " "]
shuff_list(mylist)
# ball_results = shuff_list(mylist)
print(shuff_list(mylist))


