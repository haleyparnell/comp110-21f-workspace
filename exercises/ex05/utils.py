"""List utility functions part 2."""

__author__ = "730514769"

# Define your functions below


def only_evens(list_1: list[int]) -> list[int]:
    """Given a list of ints, return only a list containing the ints that were even."""
    list_2 = []
    i: int = 0
    while len(list_1) > 0:
        if list_1[i] % 2 == 0:
            list_2.append(list_1[i])
            i += 1
    
    return list_2
