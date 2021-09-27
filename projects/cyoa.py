"""My first project."""
# Coin flip game.

__author__ = "730514769"
from random import randint

points: int = 0
player: str = ""

# Lists
majors: list[str] = ["Computer Science", "Biology"]
comp_classes: list[str] = ["COMP-110", "COMP-283", "MATH-231", "COMP-210"]
biol_classes: list[str] = ["BIOL-101", "CHEM-101", "PHYS-114", "BIOL-201"]
engl_classes: list[str] = ["ENGL-120", "ENGL-124", "ENGL-225", "ENGL-235"]
coin_list: list[str] = ["Heads [1]", "Tails [2]"]

# Emoji's used in program
HAPPYFACE: str = '\U0001F601'
COOLFACE: str = '\U0001F60E'
SADFACE: str = '\U0001F614'
COIN: str = '\U0001FA99'
CHECKMARK: str = '\U00002705'
CROSSMARK: str = '\U0000274C'
BLUSH: str = '\U0001F917'
COMPUTER: str = '\U0001F5A5'
PLANT: str = '\U0001F331'
BOOKS: str = '\U0001F4DA'


def main() -> None:
    """Entry point of program."""
    global player
    global points
    greet()
    major_choice = str(input("What is your major? Type either 'Computer Science' or 'Biology' or 'English' "))
    print(f"The major you have selected is {major_choice}.")
    if major_choice == "Computer Science":
        print(f"{player}, you're a Computer Science {COMPUTER}  major at UNC trying to register for the upcoming semester.")
        print("These are all of the courses you're trying to take:")
        i = 0
        while i < len(comp_classes):
            print(comp_classes[i])
            i = i + 1
    
        print("The first class you try to register for is COMP-110!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
        
        print("The second class you try to register for is COMP-283!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The third class you try to register for is MATH-231!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The final class you try to register for is COMP-210!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
    if major_choice == "Biology":
        print(f"{player}, you're a Biology {PLANT} major at UNC trying to register for the upcoming semester.")
        print("These are all of the courses you're trying to take:")
        i = 0
        while i < len(biol_classes):
            print(biol_classes[i])
            i = i + 1
    
        print("The first class you try to register for is BIOL-101!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
        
        print("The second class you try to register for is CHEM-101!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The third class you try to register for is PHYS-114!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The final class you try to register for is BIOL-201!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
    if major_choice == "English":
        print(f"{player}, you are an English {BOOKS} major at UNC trying to register for the upcoming semester.")
        print("These are all of the courses you're trying to take:")
        i = 0
        while i < len(engl_classes):
            print(engl_classes[i])
            i = i + 1
    
        print("The first class you try to register for is ENGL-120!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
        
        print("The second class you try to register for is ENGL-124!")
        print((f"You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The third class you try to register for is ENGl-225!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")

        print("The final class you try to register for is ENGL-235!")
        print(("You flip a coin {COIN}. Heads or tails, what is your guess?"))
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
                print(f"You have been enrolled in the class {CHECKMARK}.")
                points = points + 25
                print(f"Adventure points: {points}")
            else:
                print(f"The class is full {CROSSMARK}.")
                points = points + 0
                print(f"Adventure points: {points}")
        else:
            if coin_face == 2:
                print("Your coin landed on tails!")
                if coin_guess > 1:
                    print(f"You have been enrolled in the class {CHECKMARK}.")
                    points = points + 25
                    print(f"Adventure points: {points}")
                else:
                    print(f"The class is full {CROSSMARK}.")
                    points = points + 0
                    print(f"Adventure points: {points}")
    goodbye()


def greet() -> None:
    """Greet procedure and welcome message."""
    print(f"Welcome to UNC's new class registration system called Coin Flip! {COOLFACE}")
    print("To enroll in a class, you must land on heads during your coin flip.")
    print("Everytime you enroll in a class, you gain points. Get into all of your classes to win!")
    global player
    player = (input("But before we get started, what is your name? "))
    print(f"Hello, {player} {BLUSH}.")


def goodbye() -> None:
    """End sequence and goodbye message."""
    global player
    global points
    WINNER: int = 100
    if points == WINNER:
        print(f"Congrats!!! You have won the game! {HAPPYFACE}")
        print(f"Total score: {points}")
        print("Gameover.")
    else:
        print(f"I am sorry, you have lost UNC Coin Flip {SADFACE}.")
        print("Replay the game and reach 100 points to win.")
        print(f"Total score: {points}")
        print("Gameover.")
    replay_game: int = int(input("Would you like to play again? Type [1] for 'Yes' and [2] for 'No' "))
    if replay_game == 1:
        main()
    else:
        print("Goodbye.")


if __name__ == "__main__":
    main()
    # main function