"""List utility functions."""

__author__ = "730514769"


# TODO: Implement your functions here.

def all(user_list: list[int], user_int: int) -> bool:
    """Return True if given integer matches every value in a given list, return False otherwise or if the list is empty."""
    i: int = 0
    empty: list[int] = []
    if user_list is empty:
        return False
    if len(user_list) > 0:
        while user_list[i] > 0:
            if user_list[i] == user_int:
                i += 1
                return True
            else: 
                return False
    else:
        return False


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    i: int = 0
    x: int = 0
    total_1: int = 0
    total_2: int = 0
    while i < len(list_1):
        total_1 += list_1[i]
        i += 1
    
    while i < len(list_2):
        total_2 += list_2[x]
        x += 1

    if total_1 - total_2 == 0:
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Given a list of ints, return the largest in the list."""
    if len(input) == 0:
        raise ValueError("max)) arg is an empty List")
    else:
        input.sort()
        return input[-1]