import threading
import time
import random

tiempo = [0]
jugando = [True]

def cronometro():
    while jugando[0]:
        time.sleep(10)
        tiempo[0] += 10
        print(f"Tiempo transcurrido: {tiempo[0]} segundos")

def juego_ppt():
    opciones = ["piedra", "papel", "tijeras"]
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
        if jugador == "salir":
            jugando[0] = False
            break
        if jugador not in opciones:
            print("Opción no válida.")
            continue
        pc = random.choice(opciones)
        print(f"La computadora eligió: {pc}")
        if jugador == pc:
            print("¡Empate!")
        elif (jugador == "piedra" and pc == "tijeras") or \
             (jugador == "papel" and pc == "piedra") or \
             (jugador == "tijeras" and pc == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

hilo_tiempo = threading.Thread(target=cronometro)
hilo_tiempo.start()

juego_ppt()

hilo_tiempo.join()