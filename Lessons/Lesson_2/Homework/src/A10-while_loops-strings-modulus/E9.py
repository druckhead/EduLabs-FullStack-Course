total_p1_wins = 0
total_p2_wins = 0
total_draws = 0
total_rounds = 0

start_new_game = True
while start_new_game:
    total_rounds += 1
    player1_choice = input("Player One choice: ")
    while player1_choice != "scissors" and player1_choice != "rock" and player1_choice != "paper":
        print(f"INVALID CHOICE. CAN NOT CHOOSE {player1_choice}")
        player1_choice = input("Enter valid Player One choice: ")
    else:
        print(f"Player One chose: {player1_choice}\n")

    player2_choice = input("Player Two choice: ")
    while player2_choice != "scissors" and player2_choice != "rock" and player2_choice != "paper":
        print(f"INVALID CHOICE. CAN NOT CHOOSE {player2_choice}")
        player2_choice = input("Enter valid Player Two choice: ")
    else:
        print(f"Player Two chose: {player2_choice}\n")

    if player1_choice == "rock":
        if player2_choice == "paper":
            print("Player Two wins")
            total_p2_wins += 1
        elif player2_choice == "scissors":
            print("Player One wins")
            total_p1_wins += 1
        else:
            print("Draw")
            total_draws += 1
    elif player1_choice == "paper":
        if player2_choice == "scissors":
            print("Player Two wins")
            total_p2_wins += 1
        elif player2_choice == "rock":
            print("Player One wins")
            total_p1_wins += 1
        else:
            print("Draw")
            total_draws += 1
    else:
        if player2_choice == "rock":
            print("Player Two wins")
            total_p2_wins += 1
        elif player2_choice == "paper":
            print("Player One wins")
            total_p1_wins += 1
        else:
            print("Draw")
            total_draws += 1

    start_new_game = input("\nPlay again? (Y/N): ").strip().lower()
    while start_new_game != 'y' and start_new_game != 'n':
        start_new_game = input("Invalid input! Enter only (Y/N): ").strip().lower()
    start_new_game = True if start_new_game == 'y' else False

print(f"\n************************************\n"
      f"*                Total Stats       *\n"
      f"************************************\n"
      f"*\tRounds Played: {total_rounds}\n"
      f"*\tTotal Player One Wins: {total_p1_wins}\n"
      f"*\tTotal Player Two Wins: {total_p2_wins}\n"
      f"*\tTotal Draws: {total_draws}\n"
      f"************************************")
