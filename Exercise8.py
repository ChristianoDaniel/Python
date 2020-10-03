# Exercise 8
# Make a two-player Rock-Paper-Scissors game.
while True:
# Rules of the game.
    game_dict = {"rock" == 1,"scissors" == 2, "paper" == 3}
    game_rules = {"rock" > "scissors", "scissors" > "paper","paper" > "rock"}

    # players choice rock, paper or scissors.
    player_1 = str(input("Enter choice for player 1:\n"))
    player_2 =str(input("Enter choice for player 2:\n"))

    if player_1 > player_2:
        print("Congratulatiuons player 1.")
        if str(input("Would you like to play again, yes or no?\n")) == "yes":
            continue
        else:
            print("Game over.")
            break
    elif player_1 < player_2:
        print("Congratulatiuons player 2.")
        if str(input("Would you like to play again, yes or no?\n")) == "yes":
            continue
        else:
            print("game over.")
            break
    else:
        print("It's a draw! Please continue.")