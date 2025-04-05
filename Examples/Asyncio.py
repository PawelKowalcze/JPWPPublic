import asyncio

async def fetch_data(site):
    print(f"📡 Pobieram dane z {site}...")
    await asyncio.sleep(2)  # Symulacja operacji I/O
    print(f"✅ Pobieranie z {site} zakończone.")
    return f"Dane z {site}"

async def main():
    sites = ["example.com", "python.org", "openai.com"]
    tasks = [fetch_data(site) for site in sites]  # Tworzenie zadań
    results = await asyncio.gather(*tasks)  # Uruchomienie zadań równocześnie
    print("🎯 Wyniki:", results)

asyncio.run(main())  # Uruchomienie pętli asyncio
