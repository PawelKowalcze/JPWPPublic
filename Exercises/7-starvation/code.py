import threading
import time

lock = threading.Lock()

def high_priority_task():
    while True:
        with lock:
            print("Wysoki priorytet: uzyskał lock")
            # Simulate some work inside the critical section with a for loop


def low_priority_task():
    while True:
        with lock:
            print("Niski priorytet: uzyskał lock")
            # Simulate some work inside the critical section with a for loop



high_priority_thread = threading.Thread(target=high_priority_task)
low_priority_thread = threading.Thread(target=low_priority_task)

high_priority_thread.start()
low_priority_thread.start()