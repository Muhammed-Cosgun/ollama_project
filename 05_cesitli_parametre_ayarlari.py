import requests

# Ollama API adresi
url = "http://localhost:11434/api/chat"

# Modele gönderilecek prompt
prompt = """
Dünyanın en gereksiz süper kahramanını tasarla.
Adını, süper gücünü, zayıflığını ve sloganını yaz.
Komik olsun.
"""

# Test etmek istediğimiz parametreler
options = {
    "temperature": 0.7,       # Yaratıcılık seviyesi
    "top_p": 0.9,             # Olasılık havuzu sınırı
    "top_k": 40,              # En olası token adaylarının sayısı
    "repeat_penalty": 1.2,    # Tekrarları azaltma
    "num_predict": 300        # Maksimum üretilecek token sayısı
}

try:
    # Ollama'ya istek gönder
    response = requests.post(
        url,
        json={
            "model": "qwen3:1.7b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "options": options,
            "think": False,     # Düşünme modunu kapat
            "stream": False
        },
        timeout=120
    )

    # HTTP hatalarını kontrol et
    response.raise_for_status()

    # JSON yanıtını al
    result = response.json()

    # Test parametrelerini yazdır
    print("\n--- TEST PARAMETRELERİ ---")

    for key, value in options.items():
        print(f"{key}: {value}")

    print("think: False")
    print("--------------------------")

    # Modelin yanıtını al
    answer = result.get("message", {}).get("content", "")

    print("\n--- MODELİN YANITI ---")

    if answer.strip():
        print(answer)
    else:
        print("Model boş yanıt döndürdü.")

    # Token kullanım bilgileri
    print("\n--- TOKEN İSTATİSTİKLERİ ---")

    print("Prompt token sayısı:",
          result.get("prompt_eval_count", 0))

    print("Üretilen token sayısı:",
          result.get("eval_count", 0))

    print("Bitiş nedeni:",
          result.get("done_reason", "Bilinmiyor"))

except requests.exceptions.ConnectionError:
    print("HATA: Ollama sunucusuna bağlanılamadı.")
    print("Ollama'nın çalıştığından emin olun.")

except requests.exceptions.Timeout:
    print("HATA: Model 120 saniye içinde yanıt vermedi.")

except requests.exceptions.HTTPError as e:
    print("HTTP HATASI:", e)
    print("Sunucu yanıtı:", response.text)

except requests.exceptions.RequestException as e:
    print("İSTEK HATASI:", e)

except ValueError as e:
    print("JSON YANIT HATASI:", e)
