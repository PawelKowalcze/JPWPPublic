import threading
import time

def funkcja_watku():
    for i in range(5):
        print(f"Wątek działa: {i}")
        time.sleep(1)

# Tworzymy i uruchamiamy wątek
watek = threading.Thread(target=funkcja_watku)
watek.start()
print()
# Główny program działa równolegle
for i in range (10):
    print(f"Główny wątek: {i}")
    time.sleep(0.5)

# Czekamy na zakończenie wątku
watek.join()
print("Wątek zakończony")
