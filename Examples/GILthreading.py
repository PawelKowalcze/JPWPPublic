import threading
import os
import time

def count():
    x = 0
    for _ in range(10**8):  # Duże obciążenie procesora
        x += 1
        # print(f"Wynik: {x}, PID: {os.getpid()}")  # Zakomentowane, aby nie zaśmiecać konsoli


if __name__ == "__main__":

    start = time.time()

    # Tworzymy dwa wątki
    thread1 = threading.Thread(target=count)
    thread2 = threading.Thread(target=count)

    # Uruchamiamy oba wątki
    thread1.start()
    thread2.start()

    # Czekamy na zakończenie wątków
    thread1.join()
    thread2.join()
    end = time.time()

    print(f"Czas wykonania: {end - start:.2f} sekund")
    print("Zakończono")

