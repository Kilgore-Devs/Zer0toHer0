"""Write a function takes a two-word string
and returns True if both words begin with same letter"""


def two_strings(string):  # creates function that passes in string, in this case-two words
    # set var to str.split() which
    # splits at space and turns words into items of a list
    list_of_words = string.split()
    print(string.split())   # for demo, prints what's passed into fx as a list
    print(list_of_words[0][0] == list_of_words[1][0])  # for demo, prints true or false
    return list_of_words[0][0] == list_of_words[1][0]  # returns true or false


two_strings("zebra lizard")

two_strings("larry lizard")
