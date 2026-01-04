import random

player_score = 0
computer_score = 0

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors or quit): ").lower()
    options = ["rock", "paper", "scissors"]
    if player_choice == "quit":
        return {"player": "quit", "computer": None}
    if player_choice not in options:
        return {"player": "invalid", "computer": None}
    
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    if player == computer:
        return "tie"

    if player == "rock":
        return "win" if computer == "scissors" else "lose"

    if player == "paper":
        return "win" if computer == "rock" else "lose"

    if player == "scissors":
        return "win" if computer == "paper" else "lose"


print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type rock / paper / scissors to play — or type 'quit' to stop.\n")

while True:
    choices = get_choices()
    player = choices["player"]
    computer = choices["computer"]

    if player == "quit":
        print("\n👋 Game over — thanks for playing!")
        print(f"🏆 Final Score → You: {player_score} | Computer: {computer_score}")
        break

    if player == "invalid":
        print("⚠ Invalid choice. Please type rock, paper, or scissors.\n")
        continue

    print(f"\nYou chose {player}, computer chose {computer}.")

    result = check_win(player, computer)

    if result == "tie":
        print("🤝 It's a tie!\n")
    elif result == "win":
        print("🎉 You win this round!\n")
        player_score += 1
    else:
        print("💀 You lose this round!\n")
        computer_score += 1

    print(f"📊 Score → You: {player_score} | Computer: {computer_score}\n")
