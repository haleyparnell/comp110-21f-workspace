"""Drawing forests in a loop."""

__author__ = "730514769"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

user_word: int = int(input("Depth: "))
a: str = ""

while user_word > 0:
    a = TREE * a
    user_word = user_word - 1

print(a)