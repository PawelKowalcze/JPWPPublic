import threading
import time


semafor = threading.Semaphore(3)


def klient(id):
    semafor.acquire()  # Zajęcie zasobu
    print(f"Klient {id + 1} korzysta z zasobu.")
    time.sleep(2)
    print(f"Klient {id + 1} zwalnia zasób.")
    semafor.release()  # Zwolnienie zasobu


for i in range(6):
    threading.Thread(target=klient, args=(i,)).start()


