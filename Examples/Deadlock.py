import threading
import time

lock_A = threading.Lock()
lock_B = threading.Lock()

def watek1():
    lock_A.acquire()
    print("Wątek 1: Zajęcie lock_A")
    time.sleep(1)
    lock_B.acquire()  # Czeka na lock_B, który jest już zajęty przez watek2
    print("Wątek 1 zakończony")
    lock_B.release()
    lock_A.release()

def watek2():
    lock_B.acquire()
    print("Wątek 2: Zajęcie lock_B")
    time.sleep(1)
    lock_A.acquire()  # Czeka na lock_A, który jest już zajęty przez watek1
    print("Wątek 2 zakończony")
    lock_A.release()
    lock_B.release()

t1 = threading.Thread(target=watek1)
t2 = threading.Thread(target=watek2)

t1.start()
t2.start()

t1.join()
t2.join()
