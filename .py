import random


# =====================================
# ROCK PAPER SCISSORS FUNCTION
# =====================================
def rockPaperScissorGame():

    choices = ["rock", "paper", "scissors"]

    while True:

        print("\nPress 1 for ROCK 👊🏾")
        print("Press 2 for PAPER ✋🏾")
        print("Press 3 for SCISSORS ✌🏾")

        user_input = input("Enter choice: ")

        # VALIDATION
        if user_input not in ["1", "2", "3"]:
            print("Invalid input")
            continue

        # USER CHOICE
        user = choices[int(user_input) - 1]

        # COMPUTER CHOICE
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

        # CONTINUE OPTION
        cont = input("\nWish to continue? Y/N: ").upper()

        if cont != "Y":
            break


# =====================================
# MAIN PROGRAM
# =====================================

value = ""

name = input("Please enter your name: ")

print(f"Welcome {name} to PG games!")

print()

while True:

    print()

    value = input(
        f'Please enter the number \n'
        f'1 to play Guess game or \n'
        f'2 to play paper, rock and scissors or \n'
        f'3 to play payment or \n'
        f'Enter "Q" to quit the game: '
    ).upper()

    print()

    if value != "Q":

        # GUESS GAME
        if value == "1":

            print("Welcome to Guess Game")

            cont = ""

            while True:

                print("I am now running")

                print("Wish to continue: Y/N")

                cont = input("").upper()

                if cont == "Y":

                    for i in range(4):
                        print("RUNNING")

                else:
                    break

                print()

        # ROCK PAPER SCISSORS
        elif value == "2":

            print("Welcome to paper, rock and scissors Game")

            # FUNCTION CALL
            rockPaperScissorGame()

        # PAYMENT GAME
        elif value == "3":

            print("Welcome to payment Game")

            print("I am now running")

        else:
            print("Invalid option")

    else:
        print("Goodbye!")
        break