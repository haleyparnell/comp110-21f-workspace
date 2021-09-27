from random import randint

comp_classes: list[str] = ["COMP-110", "COMP-283", "MATH-231", "COMP-210"]
coin_list: list[str] = ["Heads [1]", "Tails [2]"]
points = 0

print("The first class you try to register for is COMP-110!")
print(("You flip a coin. Heads or tails, what is your guess?"))
i = 0
while i < len(coin_list):
    print(coin_list[i])
    i = i + 1

coin_guess: int = int(input("Type the number 1 or 2: "))
print(f"You selected {coin_guess}.")
coin_face: int = int(randint(1, 2))
if coin_face == 1:
    print("Your coin landed on heads!")
    if coin_guess < 2:
        print("You have been enrolled in the class.")
        points = points + 25
        print(f"Adventure points: {points}")
    else:
        print("The class is full.")
        points = points + 0
        print(f"Adventure points: {points}")
else:
    if coin_face == 2:
        print("Your coin landed on tails!")
        if coin_guess > 1:
            print("You have been enrolled in the class.")
            points = points + 25
            print(f"Adventure points: {points}")
        else:
            print("The class is full.")
            points = points + 0
            print(f"Adventure points: {points}")