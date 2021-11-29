"""Practice with dictionaries."""

__author__ = "730514769" 


# Define your functions below
def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values."""
    final_dict = {v: k for k, v in my_dict.items()}
    return final_dict


def favorite_color(user: dict[str, str]) -> str:
    """Find the most popular favorite color."""
    color = max(list(user.values()), key=list(user.values()).count)
    return color


def count(my_list: list[str]) -> dict[str, int]:
    """On your own."""
    freq = dict()
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
