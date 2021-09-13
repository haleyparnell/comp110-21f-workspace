"""Counting letters in a string."""

__author__ = "730514769"

search_letter: str = input("What letter do you want to search for?: ")
user_word: str = input("Enter a word: ")

word = user_word
character = search_letter

counter = 0

while character in word:
    if character in word is True:
        counter = 0 + 1
    else:
        counter = 0

print("Count:", counter)