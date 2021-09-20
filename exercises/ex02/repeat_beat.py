"""Repeating a beat in a loop."""

__author__ = "730514769"

beat_name: str = input("What beat do you want to repeat? ")
beat_times: str = input("How many times do you want to repeat it? ")
choice = int(beat_times) 

a: str = ""

if choice <= 0:
    print("No beat...")
else:
    while choice > 0:
        a = beat_name + a
        choice = choice - 1

    print(a)