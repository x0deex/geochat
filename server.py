import socket

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Сервер запущен на порту {PORT}. Ждём подключения...")

conn, addr = server.accept()
print(f"[+] Подключился: {addr}")

# === Первое сообщение — это всегда IP клиента ===
client_info = conn.recv(1024).decode('utf-8')
print(f"[i] Данные клиента: {client_info}")

# === Дальше — обычные сообщения ===
while True:
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"[Клиент]: {data}")

conn.close()
server.close()