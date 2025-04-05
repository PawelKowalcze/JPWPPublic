import sqlite3

# Połączenie z bazą danych (utworzy plik bank.db, jeśli nie istnieje)
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Tworzenie tabeli kont (jeśli nie istnieje)
cursor.execute("""
CREATE TABLE IF NOT EXISTS konta (
    id INTEGER PRIMARY KEY,
    imie TEXT,
    saldo REAL
)
""")
conn.commit()

# Dodanie przykładowych kont (tylko raz)
cursor.execute("INSERT OR IGNORE INTO konta (id, imie, saldo) VALUES (1, 'Alicja', 1000.0)")
cursor.execute("INSERT OR IGNORE INTO konta (id, imie, saldo) VALUES (2, 'Bartek', 500.0)")
conn.commit()

cursor.execute("SELECT * FROM konta")
for row in cursor.fetchall():
    print(row)

# 📌 Funkcja do przelewu pieniędzy
def przelew(kwota, z_id, do_id):
    try:
        # Rozpoczęcie transakcji
        conn.execute("BEGIN TRANSACTION;")

        # Pobranie salda nadawcy
        cursor.execute("SELECT saldo FROM konta WHERE id = ?", (z_id,))
        saldo_nadawcy = cursor.fetchone()[0]

        if saldo_nadawcy < kwota:
            raise ValueError("Brak wystarczających środków!")

        # Aktualizacja sald w bazie
        cursor.execute("UPDATE konta SET saldo = saldo - ? WHERE id = ?", (kwota, z_id))
        cursor.execute("UPDATE konta SET saldo = saldo + ? WHERE id = ?", (kwota, do_id))

        # Zatwierdzenie transakcji (jeśli wszystko poszło dobrze)
        conn.commit()
        print("✅ Przelew zakończony sukcesem!")

    except Exception as e:
        # Cofnięcie transakcji w przypadku błędu
        conn.rollback()
        print(f"❌ Błąd: {e}, przelew anulowany.")

# 📌 Wykonanie przykładowej transakcji

kwota = int(input("Podaj kwotę przelewu: "))
z_id = int(input("Podaj ID nadawcy: "))
do_id = int(input("Podaj ID odbiorcy: "))
przelew(kwota, z_id, do_id)

# Wyświetlenie aktualnych sald
cursor.execute("SELECT * FROM konta")
for row in cursor.fetchall():
    print(row)

# Zamknięcie połączenia
conn.close()
