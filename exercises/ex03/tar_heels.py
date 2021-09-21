"""An exercise in remainders and boolean logic."""

__author__ = "730514769"


user_integer: int = int(input("Enter an int: "))

if (user_integer % 2 == 0) and (user_integer % 7 == 0):
    print("TAR HEELS")
else:
    if user_integer % 2 == 0:
        print("TAR")
    else:
        if user_integer % 7 == 0:
            print("HEELS")
        else:
            if (user_integer % 2 != 0) and (user_integer % 7 != 0):
                print("CAROLINA")