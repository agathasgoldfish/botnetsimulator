import socket
import time

HOST = '127.0.0.1'
PORT = 9999

while True:
    try:
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bot.connect((HOST, PORT))
        print("[*] Connected to C2 Server")

        while True:
            command = bot.recv(1024).decode()
            print(f"[+] Received command: {command}")
            if command == "ping":
                bot.send("pong".encode())
            elif command == "status":
                bot.send("Bot running normally.".encode())
            else:
                bot.send(f"Unknown command: {command}".encode())

    except Exception as e:
        print(f"[!] Connection lost. Reconnecting in 3 seconds... ({e})")
        time.sleep(3)
