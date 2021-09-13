"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730514769"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
choice: int = int(randint(1, 20))
if choice < 5:
    print("Your life will be filled with great happiness.")
else:
    if choice < 10:
        print("An unspeakable amount of riches will soon approach.")
    else:
        if choice < 15:
            print("You should enter the lottery.")
        else: 
            print("You will have a great day.")
print("Now, go spread positive vibes!")