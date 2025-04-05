import threading

lock = threading.Lock()

def thread_task():
    print()
    # Dodaj kod tutaj


threads = [threading.Thread(target=thread_task) for _ in range(2)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()