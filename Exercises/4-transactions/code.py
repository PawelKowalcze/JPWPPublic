import threading

balance = 100
lock = threading.Lock()

def deposit(amount):
    global balance
    with lock:
        print()
        # Dodaj kod tutaj


def withdraw(amount):
    global balance
    with lock:
        print()
        # Dodaj kod tutaj


threads = [
    threading.Thread(target=deposit, args=(50,)),
    threading.Thread(target=withdraw, args=(30,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()