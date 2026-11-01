import requests

URL = "http://localhost:11434/api/chat"

# 1. Değişkenleri ve promptu dışarıda tanımlayın
talep = "finans raporu çok yavaş açılıyor ve gösterilen satış tutarları da yanlış"

prompt = f"""
Aşağıdaki teknik destek talebini analiz et.

Talep: {talep}

Kategori yalnızca şunlardan biri olabilir:
Erişim, Performans, Veri Kalitesi, Diğer

Öncelik yalnızca:
Düşük, Orta, Yüksek

Şu alanlarla JSON üret:
kategori, oncelik, gerekce, eksik_bilgiler

eksik_bilgiler bir liste olmalıdır.
Bilgi uydurma.
"""

# 2. JSON payload yapısını temiz bir şekilde oluşturun
payload = {
    "model": "qwen3:1.7b",
    "messages": [
        {
            "role": "user", 
            "content": prompt
        }
    ],
    "stream": False
}

# 3. İsteği gönderin
response = requests.post(URL, json=payload, timeout=180)
response.raise_for_status()

print(response.json()["message"]["content"])