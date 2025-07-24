# Rock, Paper, Scissors (with Timer)

This is a simple **Rock, Paper, Scissors** game for the console, written in Python.  
It includes a timer that shows the elapsed time every 10 seconds while you play.

## How does it work?

- The game asks you to choose between `rock`, `paper`, or `scissors`.
- The computer randomly selects an option.
- The winner of each round is displayed.
- You can exit the game by typing `salir` (Spanish for "exit").
- While you play, a timer runs in the background and prints the total elapsed time every 10 seconds.

## How to run

1. Make sure you have Python 3 installed.
2. Run the file in your terminal:
   ```
   python PiedraPapelTijeras.py
   ```
3. Play and watch the elapsed time appear in the console.

## Main features

- Uses **threads** (`threading`) to run the timer and the game simultaneously.
- The timer stops automatically when you exit the game.

---

Have fun playing and see how much time you spend!