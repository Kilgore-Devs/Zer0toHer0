from random import shuffle
the_list = [" ", "X", " "]


def shuffler(the_list):  # shuffles list
    shuffle(the_list)

    return the_list  # returns shuffled version of list


shuffler(the_list)


def the_guess():
    user_guess = ""

    while user_guess not in ["0", "1", "2"]:
        user_guess = input("Pick one of the following numbers: 0 , 1, or 2  ")  # user input returns a string

    return int(user_guess)


# my_index = the_guess()

def guess_checker(the_list, user_guess):
    if the_list[user_guess] == "X":
        print("Nailed it!")
    elif the_list[user_guess] != "X":
        print("Wrong choice.")
        the_guess()
        shuffler(the_list)
        guess_checker(mixed_list, users_guess)
    else:
        return False


# set up initial list
the_list = [" ", "X", " "]

# shuffle list
mixed_list = shuffler(the_list)

# user guess
users_guess = the_guess()

# check guess
guess_checker(mixed_list, users_guess)
