import random


def get_choices():
  player_choice = input("enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return (f"you win! {player} beats {computer}")
    else:
      return "Paper covers rock. You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock. You win!"
    else:
      return "Scissors cuts paper. You lose."
  elif player == "seissors":
    if computer == "paper":
      return "Scissors cuts paper. You win!"
    else:
      return "Rock smashes scissors. You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
