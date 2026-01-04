# 🪨 Rock • 📄 Paper • ✂️ Scissors — Python Game  

<div align="center">

🎮 A fun beginner-friendly Python project  
💡 Practice loops • conditionals • random module  
🔥 Includes score tracking + infinite gameplay  

</div>

---

## 🌟 Features

✨ **Case-Insensitive Input** — `Rock`, `rock`, `ROCK` (all work!)  
✨ **Scoreboard** — Tracks player vs computer  
✨ **Plays Until You Quit** — press `q` anytime  
✨ **Beginner-Friendly** — Clean & readable code  
✨ **Error-Handled** — Invalid inputs don’t crash the game  

---

## 🧠 Game Rules

| Player Choice | Beats |
|--------------|-------|
| 🪨 Rock      | ✂️ Scissors |
| 📄 Paper     | 🪨 Rock |
| ✂️ Scissors  | 📄 Paper |

😐 Same choices → **Tie**

---

## 🚀 Run the Game

### ▶️ Step 1 — Save as:
```
rock_paper_scissors.py
```

### ▶️ Step 2 — Run in VS Code terminal
```
python rock_paper_scissors.py
```
or
```
python3 rock_paper_scissors.py
```

---

## 🧾 Source Code

```python
import random

player_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Enter rock / paper / scissors or q to quit: ").lower()

    if player_choice == "q":
        print("Game Over 👋")
        print(f"Final Score → You: {player_score} | Computer: {computer_score}")
        break

    if player_choice not in options:
        print("Invalid choice ❌ Try again!")
        continue

    computer_choice = random.choice(options)
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Result: It's a tie 😐")

    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You win 🎉")
        player_score += 1
    else:
        print("Result: Computer wins 🤖")
        computer_score += 1

    print(f"Score → You: {player_score} | Computer: {computer_score}\n")
```

## 🧩 What You’ll Learn

✔ Variables  
✔ Loops  
✔ Conditionals  
✔ Random module  
✔ Score logic  
✔ Input handling  
✔ Breaking loops  

Perfect for **students & interview prep** 🎯  

---

## 🛠 Tech Used

🐍 Python 3  
🧠 Logic & Problem Solving  

---

## 🚀 Future Enhancements

🔹 Add GUI (Tkinter / PyGame)  
🔹 Add sound effects  
🔹 Multiplayer mode  
🔹 Difficulty levels  

---

## ❤️ Contribute / Share

If this helped you —  
⭐ **Star this repo**  
🍴 **Fork it**  
📝 **Use it for practice & learning**

Let’s grow together 🚀  
