"""List utility functions part 2."""

__author__ = "730514769"

# Define your functions below


def only_evens(list_1: list[int]) -> list[int]:
    """Given a list of ints, return only a list containing the ints that were even."""
    list_1 = [x for x in list_1 if x % 2 != 0]
    return list_1


def sub(a_list: list[int], user_int_1: int, user_int_2: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    return(a_list[user_int_1:user_int_2])


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    return first_list + second_list