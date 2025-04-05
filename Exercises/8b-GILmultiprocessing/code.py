import multiprocessing
import os
import time

def count():

    x = 0
    # Zasymuluj duże obciążenie procesora pętlą for
    # Dodaj kod tutaj


if __name__ == "__main__":
    start = time.time()
    process1 = multiprocessing.Process(target=count)
    process2 = multiprocessing.Process(target=count)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    end = time.time()

    print(f"Czas wykonania: {end - start:.2f} sekund")
    print("Zakończono")