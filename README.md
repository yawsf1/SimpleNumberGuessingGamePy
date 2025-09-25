# Number Guessing Game

## Overview
This is a simple Python console game where the player tries to guess a randomly generated number between 1 and 100. The program gives feedback on how close the guess is and tracks the number of attempts and score.

---

## Features
- Random number generation between 1 and 100
- User inputs guesses via the console
- Feedback on guesses:
  - "Too big" / "Bigger a bit"
  - "Too small" / "Smaller a bit"
- Tracks number of attempts
- Tracks score (increments when player guesses correctly)
- Handles invalid input gracefully

---

## How to Run
1. Make sure you have Python 3 installed.
2. Run the program:
   python guess_game.py
   
3. Follow the prompts and try to guess the number.

## Example Gameplay

Entrer a number between 1 and 100: 50
Too big
attempts: 1

Entrer a number between 1 and 100: 20
Too small
attempts: 2

Entrer a number between 1 and 100: 35
Bigger a bit
attempts: 3

Entrer a number between 1 and 100: 37
Congrats you did win
Your score now is 1
And your attempts are: 3

## Dependencies
Python 3.x
