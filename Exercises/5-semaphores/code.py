import threading
import time

semaphore = threading.Semaphore(2)  # Allow only 2 threads to access the critical section simultaneously

def thread_task():
    print(f"Wątek {threading.get_ident()} próbuje uzyskać semafor")
    with semaphore:
        print()
        #Dodaj kod tutaj

threads = [threading.Thread(target=thread_task) for _ in range(5)]  # Increase the number of threads

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()