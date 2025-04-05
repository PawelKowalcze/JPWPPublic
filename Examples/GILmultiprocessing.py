import multiprocessing
import os
import time

def count():
    x = 0
    for _ in range(10**8):
        x += 1
        # print(f"Wynik: {x}, PID: {os.getpid()}")


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
