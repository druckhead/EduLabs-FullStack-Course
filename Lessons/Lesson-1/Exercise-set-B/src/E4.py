player1_choice = input("Player one choice: ")
print(player1_choice)
if player1_choice != "scissors" and player1_choice != "rock" and player1_choice != "paper":
    print(f"INVALID CHOICE. CAN NOT CHOOSE {player1_choice}")
    exit(1)
else:
    print(f"Player one chose: {player1_choice}")
    
player2_choice = input("Player two choice: ")
if player2_choice != "scissors" and player2_choice != "rock" and player2_choice != "paper":
    print(f"INVALID CHOICE. CAN NOT CHOOSE {player2_choice}")
    exit(1)
else:
    print(f"Player two chose: {player2_choice}")

if player1_choice == "rock":
    if player2_choice == "paper":
        print("player 2 wins")
    elif player2_choice == "scissors":
        print("player 1 wins")
    else:
        print("draw")
elif player1_choice == "paper":
    if player2_choice == "scissors":
        print("player 2 wins")
    elif player2_choice == "rock":
        print("player 1 wins")
    else:
        print("draw")
else:
    if player2_choice == "rock":
        print("player 2 wins")
    elif player2_choice == "paper":
        print("player 1 wins")
    else:
        print("draw")
