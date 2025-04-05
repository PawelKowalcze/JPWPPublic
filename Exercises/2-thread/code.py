import threading

def task():
    print()
    # Dodaj kod tutaj


threads = [threading.Thread(target=task) for _ in range(2)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()