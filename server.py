import socket
import threading

HOST = '127.0.0.1'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[+] C2 Server listening on {HOST}:{PORT}")

bots = []

def handle_bot(bot, addr):
    print(f"[+] Bot connected from {addr}")
    while True:
        try:
            # Wait for command from main thread (via input)
            pass  # We'll handle commands globally instead
        except:
            print(f"[-] Bot {addr} disconnected")
            bots.remove(bot)
            bot.close()
            break

def broadcast_command(command):
    for bot in bots[:]:
        try:
            bot.send(command.encode())
            response = bot.recv(1024).decode()
            print(f"[BOT {bot.getpeername()}] {response}")
        except:
            print(f"[-] Lost connection to bot {bot.getpeername()}")
            bots.remove(bot)
            bot.close()

def accept_bots():
    while True:
        client, addr = server.accept()
        bots.append(client)
        threading.Thread(target=handle_bot, args=(client, addr), daemon=True).start()

# Start accepting bots in a background thread
threading.Thread(target=accept_bots, daemon=True).start()

# Main thread handles user input to send commands
while True:
    command = input("Enter command to send to bots: ")
    if command.strip():
        broadcast_command(command)

