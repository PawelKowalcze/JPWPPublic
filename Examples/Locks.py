import threading

# Wspólna zmienna
licznik = 0

# Tworzymy blokadę
lock = threading.Lock()

def zwieksz_licznik():
    global licznik
    for _ in range(1000000):
        with lock:  # Blokujemy dostęp do zasobu
            licznik += 1

# Tworzymy dwa wątki
watek1 = threading.Thread(target=zwieksz_licznik)
watek2 = threading.Thread(target=zwieksz_licznik)

# Uruchamiamy wątki
watek1.start()
watek2.start()

# Czekamy na zakończenie wątków
watek1.join()
watek2.join()

print(f"Końcowa wartość licznika: {licznik}")
