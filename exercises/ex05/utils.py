"""List utility functions part 2."""

__author__ = "730514769"

# Define your functions below


def only_evens(list_1: list[int]) -> list[int]:
    """Given a list of ints, return only a list containing the ints that were even."""
    list_2 = []
    i: int = 0
    while i < len(list_1):
        if list_1[i] % 2 == 0:
            list_2.append(list_1[i])
            i += 1
    
    return list_2


def sub(a_list: list[int], user_int_1: int, user_int_2: int) -> list[int]:
    final_list = []
    start, end = user_int_1, user_int_2
    if start < end:
        a_list.extend(range(start, end))
        a_list.append(end)
    
    return final_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    return first_list + second_list