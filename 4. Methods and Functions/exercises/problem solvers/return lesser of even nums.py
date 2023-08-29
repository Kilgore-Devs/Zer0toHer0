"""Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd"""


def lesser_of_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print(a, b)
        return min(a, b)
    else:
        print(max(a, b))
        return max(a, b)


lesser_of_evens(777, 888)
