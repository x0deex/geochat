import socket
import requests

# === 1. Узнаём свой публичный IP и геолокацию ===
try:
    ip = requests.get('https://api.ipify.org', timeout=5).text
    geo = requests.get(f'http://ip-api.com/json/{ip}', timeout=5).json()
    city = geo.get('city', '?')
    country = geo.get('country', '?')
    lat = geo.get('lat', '?')
    lon = geo.get('lon', '?')
except Exception as e:
    ip, city, country, lat, lon = 'unknown', '?', '?', '?', '?'
    print(f"[!] Не удалось получить IP: {e}")

info = f"IP={ip} | {city}, {country} | {lat},{lon}"
print(f"[i] Твои данные: {info}")

# === 2. Подключаемся к серверу ===
HOST = '192.168.1.3'   # IP ПК, где запущен сервер
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# === 3. Автоматически отправляем IP и геолокацию ===
client.send(info.encode('utf-8'))
print("[+] Подключено. Данные отправлены. Пиши сообщения:")

# === 4. Чат ===
while True:
    msg = input("Ты: ")
    if msg.lower() == 'exit':
        break
    client.send(msg.encode('utf-8'))

client.close()