import requests
import time
from datetime import datetime

# 🌐 URL dell'API per il mining
URL = "https://nnc.ftwapps.lol/api/user/ack"

# 🛠️ Header con il tuo token di autenticazione
HEADERS = {
    "Authorization": "c86f7bddd2dc828851a90aa6c2d17dea",  # Cambia con il tuo token
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Origin": "https://nnc.ftwapps.lol"
}

# ⚙️ Dati della richiesta
DATA = {
    "clicks": 10,  
    "tg_user_id": 741481460  # Cambia con il tuo Telegram ID
}

def tempo_prossima_ora():
    """ 🕒 Calcola quanti secondi mancano alla prossima ora esatta """
    now = datetime.now()
    minuti_mancanti = 60 - now.minute
    secondi_mancanti = (minuti_mancanti * 60) - now.second
    return secondi_mancanti

def minare():
    counter = 1  # 🔢 Contatore dei tentativi di mining
    
    while True:
        try:
            response = requests.post(URL, headers=HEADERS, json=DATA)

            if response.status_code == 200:
                print(f"✅ {counter} - Mining effettuato con successo!")
            elif response.status_code == 400:
                # ⚠️ Energia esaurita, aspetta fino all'ora successiva
                attesa = tempo_prossima_ora()
                print(f"⚠️ Energia esaurita! Aspetto fino alla prossima ora...")
                for sec in range(attesa, 0, -1):
                    minuti = sec // 60
                    secondi = sec % 60
                    print(f"\r⏳ Tempo rimanente: {minuti} min {secondi} sec...", end="", flush=True)
                    time.sleep(1)
                print("\n🔋 Energia ricaricata! Riprendo il mining...")
            else:
                print(f"❌ Errore {response.status_code}: {response.text}")

        except Exception as e:
            print(f"❌ Errore nella richiesta: {e}")

        counter += 1  # 🔢 Incrementa il contatore

# 🚀 Avvia il mining senza limiti di velocità!
minare()