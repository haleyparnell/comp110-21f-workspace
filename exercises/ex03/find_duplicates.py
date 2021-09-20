"""Finding duplicate letters in a word."""

__author__ = "730514769"

user_word: str = input("Enter a word: ")


def duplicate_count(text):
    seen = set()
    return len({char for char in text if char in seen or seen.add(char) is not None})


dup_let: int = (duplicate_count(user_word))

if dup_let > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")