"""Practice with dictionaries."""

__author__ = "730514769"


# Define your functions below
def invert(user: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values."""
    user = {v: k for k, v in user.items()}
    print(user)