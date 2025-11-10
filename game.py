# game.py
# --- GenAI Acknowledgment ---
# Code co-created by Gemini (version Pro 2.5, Google, https://gemini.google.com).
# -----------------------------

import random
import os

def get_high_score(score_file="high_score.txt"):
    try:
        with open(score_file, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 999 
    except ValueError:
        print("\n[Warning: High score file corrupted. Resetting.]")
        return 999 
    except Exception as e:
        print(f"\n[Warning: An unexpected file error occurred: {e}]")
        return 999

def save_high_score(new_score, score_file="high_score.txt"):
    try:
        with open(score_file, 'w') as f:
            f.write(str(new_score))
    except IOError:
        print("\n[Error: Could not save high score due to file write failure.]")

class GuessingGame:
    def __init__(self, low=1, high=100):
        self.low = low; self.high = high; self.target = random.randint(self.low, high); self.guesses = 0
        print(f"I'm thinking of a number between {self.low} and {self.high}. Type 'exit' to quit.")
    
    def play(self):
        while True:
            try:
                user_input = input("Enter your guess: ").strip().lower()
                
                if user_input == 'exit':
                    print("\nExiting game. Goodbye!")
                    return None 
                
                guess = int(user_input)
                self.guesses += 1
            except ValueError: 
                print("Invalid input. Please enter a whole number or 'exit'.")
                continue

            if guess < self.target:
                print("Too low! Try again.")
            elif guess > self.target:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number {self.target} in {self.guesses} guesses.")
                return self.guesses 

def main():
    print("--- Guess The Number Game ---")
    
    current_best = get_high_score()
    if current_best != 999:
        print(f"Current best score (fewest guesses): {current_best}")
    
    game = GuessingGame()
    score = game.play()

    if score is not None:
        if score < current_best:
            print("NEW BEST SCORE! Saving your score.")
            save_high_score(score)
        elif current_best != 999:
            print(f"The best score remains: {current_best}")

if __name__ == "__main__":
    main()