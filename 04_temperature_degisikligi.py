import requests

url = "http://localhost:11434/api/chat"

prompt = """
Dünyanın en gereksiz süper kahramanını tasarla.
Adını, süper gücünü, zayıflığını ve sloganını yaz.
Komik olsun.
"""

for sicaklik in [0.1, 0.7, 1.3]:
    response = requests.post(
        url,
        json={
            "model": "qwen3:1.7b",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "options": {
                "temperature": sicaklik
            },
            "stream": False
        },
        timeout=120
    )
    
    response.raise_for_status()
    
    print(f"\nTEMPERATURE = {sicaklik}")
    print(response.json()["message"]["content"])