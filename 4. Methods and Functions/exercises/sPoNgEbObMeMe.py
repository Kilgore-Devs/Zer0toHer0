
def spongebob(anything):

    result = ""
    for i, letters in enumerate(anything):
        if i % 2 == 0:
            result += letters.lower()
        else:
            result += letters.upper()
    return result


meme = input("Input a phrase here:   ")
print(spongebob(meme))
