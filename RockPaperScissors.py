import random


# optional - how many rounds? best of 3, 5, 7 etc...

# prompt user for rock paper scissor choice
def get_user_hand():
    return str(input("Would you like to do rock, paper or scissors: "))


# get computer random rock paper scissor choice
def get_computer_hand():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "rock"
    elif random_number == 2:
        return "paper"
    elif random_number == 3:
        return "scissors"
    else:
        raise Exception(f"number out of bounds, should be 1-3, got {random_number}")


# check to see who wins
def get_winner(human_choice, computer_choice):
    # check for draw
    if human_choice == computer_choice:
        return "draw"
    # human rock, computer scissors
    elif human_choice == "rock" and computer_choice == "scissors":
        return "human"
    # human scissors, computer is paper
    elif human_choice == "scissors" and computer_choice == "paper":
        return "human"
    # human paper, computer is rock
    elif human_choice == "paper" and computer_choice == "rock":
        return "human"
    # computer wins
    else:
        return "computer"


# main game run
def run_game_round():
    human_choice = get_user_hand()
    computer_choice = get_computer_hand()
    winner = get_winner(human_choice, computer_choice)
    print(f"human picked: {human_choice} \n computer picked: {computer_choice} \n winner: {winner} ")
    return winner


# optional - check to see if they or the computer has won the series

# first to 2 wins
human_wins = 0
computer_wins = 0
game_winner = "no_one"
while game_winner == "no_one":
    round_winner = run_game_round()
    if round_winner == "human":
        human_wins += 1
        if human_wins == 2:
            game_winner = round_winner
    elif round_winner == "computer":
        computer_wins += 1
        if computer_wins == 2:
            game_winner = round_winner
print(f"human score: {human_wins} \n computer score: {computer_wins} \n winner: {game_winner}")
