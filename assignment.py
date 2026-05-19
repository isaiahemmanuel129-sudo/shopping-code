import random



def guessGame():

    while True:

        comp = random.randint(1, 10)

        print("\n🎮 Guess a number between 1 and 10")
        print("You have 4 attempts!")

        # FOR LOOP
        for i in range(4):

            userInput = input("Enter your guess: ")

            # check if input is number
            if not userInput.isdigit():
                print("❌ Invalid input")
                continue

            userInput = int(userInput)

            if userInput == comp:
                print(" Correct! You win!")
                break

            elif userInput < comp:
                print(" Too low!")

            else:
                print(" Too high!")

        else:
            print(f" Game Over! The number was {comp}")

        cont = input("\nWish to continue? Y/N: ").upper()

        if cont != "Y":
            break



def rockPaperScissorGame():

    choices = ["rock", "paper", "scissors"]

    while True:

        print("\nPress 1 for ROCK 👊🏾")
        print("Press 2 for PAPER ✋🏾")
        print("Press 3 for SCISSORS ✌🏾")

        user_input = input("Enter choice: ")

        if user_input not in ["1", "2", "3"]:
            print("❌ Invalid input")
            continue

        user = choices[int(user_input) - 1]
        comp = random.choice(choices)   

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {comp}")

        # DRAW
        if user == comp:
            print("🤝 It's a draw!")

        # USER WINS
        elif (
            (user == "rock" and comp == "scissors") or
            (user == "paper" and comp == "rock") or
            (user == "scissors" and comp == "paper")
        ):
            print("🎉 You win!")

        # COMPUTER WINS
        else:
            print("💻 Computer wins!")

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

    # GUESS GAME
    if value == "1":

        print("\nWelcome to Guess Game")
        guessGame()

    # ROCK PAPER SCISSORS
    elif value == "2":

        print("\nWelcome to Rock Paper Scissors Game")
        rockPaperScissorGame()

    # PAYMENT
    elif value == "3":

        print("\nWelcome to Payment Game")

    # QUIT
    elif value == "Q":

        print("👋 Goodbye!")
        break

    # INVALID INPUT
    else:

        print("❌ Invalid option")