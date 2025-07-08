import threading
import time
import random

# Shared variables for timer and game state
tiempo = [0]        # Elapsed time in seconds (as a mutable list)
jugando = [True]    # Game running flag (as a mutable list)

def cronometro():
    """
    Timer function that runs in a separate thread.
    Every 10 seconds, it increases the elapsed time and prints it.
    Stops when the game ends.
    """
    while jugando[0]:
        time.sleep(10)
        tiempo[0] += 10
        print(f"Elapsed time: {tiempo[0]} seconds")

def juego_ppt():
    """
    Main Rock, Paper, Scissors game loop.
    - Prompts the user to choose 'piedra' (rock), 'papel' (paper), or 'tijeras' (scissors).
    - The computer randomly selects its choice.
    - Prints the result of each round.
    - Type 'salir' to exit the game.
    """
    opciones = ["piedra", "papel", "tijeras"]
    while True:
        jugador = input("Choose piedra (rock), papel (paper), or tijeras (scissors) (or 'salir' to quit): ").lower()
        if jugador == "salir":
            jugando[0] = False
            break
        if jugador not in opciones:
            print("Invalid option.")
            continue
        pc = random.choice(opciones)
        print(f"The computer chose: {pc}")
        if jugador == pc:
            print("It's a tie!")
        elif (jugador == "piedra" and pc == "tijeras") or \
             (jugador == "papel" and pc == "piedra") or \
             (jugador == "tijeras" and pc == "papel"):
            print("You win!")
        else:
            print("You lose!")

# Start the timer thread
hilo_tiempo = threading.Thread(target=cronometro)
hilo_tiempo.start()

# Start the game
juego_ppt()

# Wait for the timer thread to finish before exiting
hilo_tiempo.join()
