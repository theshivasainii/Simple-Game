import random
def play_sps():
    options = ["stone", "paper", "scissors"]

    user = input("Enter stone/paper/scissors: ").lower()
    if user not in options:
        print("Invalid choice")
        return

    computer = random.choice(options)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Result: Draw")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win 🎉")
    else:
        print("Result: Computer Wins 🤖")
def play_dice():
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", user_roll)
    print("Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("Result: You Win 🎉")
    elif user_roll < computer_roll:
        print("Result: Computer Wins 🤖")
    else:
        print("Result: Draw")
def game_menu():
    while True:
        print("\n===== GAME MENU =====")
        print("1. Stone-Paper-Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input")
            continue

        if choice == 1:
            play_sps()
        elif choice == 2:
            play_dice()
        elif choice == 3:
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice")

game_menu()