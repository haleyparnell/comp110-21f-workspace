"""Counting letters in a string."""

__author__ = "730514769"

search_letter: str = input("What letter do you want to search for?: ")
user_word: str = input("Enter a word: ")

i: int = 0

while i < len(search_letter):
    if len(search_letter) > 0:
        i = user_word.count(search_letter)
<<<<<<< HEAD
   
=======

>>>>>>> 9aa29c56ac712991337466fd0741f28d5296aa37
print("Count:", i)