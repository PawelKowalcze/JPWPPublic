import threading
import time

lock = threading.Lock()

def zadanie_duze():
    while True:
        with lock:
            print("🔴 Długie zadanie działa...")
            time.sleep(5)  # Długie zadanie trwa długo

def zadanie_male():
    while True:
        with lock:
            print("🟢 Małe zadanie działa!")
            time.sleep(0.5)  # Krótkie zadanie trwa krótko

t1 = threading.Thread(target=zadanie_duze)
t2 = threading.Thread(target=zadanie_male, daemon=True)  # Małe zadanie działa cały czas

t1.start()
t2.start()
