import random

import random


def rockPaperScissorGame():

    choices = ["rock", "paper", "scissors"]

    while True:

        print("\nPress 1 for ROCK 👊🏾")
        print("Press 2 for PAPER ✋🏾")
        print("Press 3 for SCISSORS ✌🏾")

        user_input = input("Enter choice: ")

        if user_input not in ["1", "2", "3"]:
            print("Invalid input")
            continue

        user = choices[int(user_input) - 1]
        comp = random.choice(choices)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {comp}")

        # DRAW
        if user == comp:
            print("It's a draw!")

        # USER WINS
        elif (
            (user == "rock" and comp == "scissors") or
            (user == "paper" and comp == "rock") or
            (user == "scissors" and comp == "paper")
        ):
            print("You win!")

        # COMPUTER WINS
        else:
            print("Computer wins!")

        cont = input("\nWish to continue? Y/N: ").upper()

        if cont != "Y":
            break


name = input("Please enter your name: ")

print(f"\nWelcome {name} to PG Games!")

while True:

    value = input(
        '\nEnter:\n'
        '1 to play Guess Game\n'
        '2 to play Rock Paper Scissors\n'
        '3 to play Payment Game\n'
        'Q to Quit\n\n'
        'Choice: '
    ).upper()

    if value == "1":
        print("Welcome to Guess Game")

    elif value == "2":
        print("Welcome to Rock Paper Scissors Game")
        rockPaperScissorGame()

    elif value == "3":
        print("Welcome to Payment Game")

    elif value == "Q":
        print("Goodbye!")
        break

    else:
        print("Invalid option")











value = ""
name = input("Please enter your name: ")
print(f"Welcome {name} to PG games!")
print()
while True:
    print()

    value = input(f'Please enter the number \n1 to play Guess game or \n2 to play paper, rock and scissors or \n3 to play pyment or \nEnter "Q" to quit the game: ').upper()
    print()
    
    if value != "Q":

        if value == "1":
            print("Welcome to Guess Game")
            print("I am now running")
            cont = ""
            while True:
                print("wish to continue: Y/N: ")
                cont = input("").upper()
                if cont == "Y":
                    for i in range(4):
                        print("RUNNING")
                else:
                    break
                print()                

        elif value == "2":
            print("Welcome to paper, rock and scissors Game")
            print("I am now running")
        elif value == "3":
            print("Welcome to pyment Game")
            print("I am now running")
    
    else:
        break