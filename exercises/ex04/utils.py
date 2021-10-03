"""List utility functions."""

__author__ = "730514769"


# TODO: Implement your functions here.
def main() -> None:
    """Entrypoint of program."""
    x: list[int] = []
    y: int = int(input(""))


def all(user_int: int, user_list: list[int]) -> bool:
    """Return True if all numbers match the indicated number, Return False otherwise or if the list is empty."""
    i: int = 0
    while i < len(user_list):
        item: int = user_list[i]
        if item == user_int:
            return True
        i += 1

    return False