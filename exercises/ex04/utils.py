"""List utility functions."""

__author__ = "730514769"


# TODO: Implement your functions here.

def all_same(list):
    user_list: list[int] = []
    result = all(element == user_list[0] for element in user_list)
    if (result):
        return True
    else:
        return False