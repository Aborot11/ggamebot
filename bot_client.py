import socket
import time

host = "172.20.10.2"  
port = 7777


s = socket.socket()
s.connect((host, port))


difficulty_prompt = s.recv(1024).decode().strip()
print(f"[SERVER] {difficulty_prompt}")


difficulty = "3"  # You can change to "1" or "2" if needed
difficulty_map = {"1": "Easy (1–10)", "2": "Medium (1–50)", "3": "Hard (1–100)"}
print(f"[BOT] Selected Difficulty: {difficulty_map[difficulty]}")
s.sendall(difficulty.encode())


banner = s.recv(1024).decode().strip()
print(f"[SERVER] {banner}")


if difficulty == "1":
    low, high = 1, 10
elif difficulty == "2":
    low, high = 1, 50
else:
    low, high = 1, 100


while True:
    guess = (low + high) // 2
    print(f"[BOT] Guessing: {guess}")
    s.sendall(str(guess).encode())

    response = s.recv(1024).decode().strip()
    print(f"[SERVER] {response}")

    if "CORRECT!" in response:
        break
    elif "Higher" in response:
        low = guess + 1
    elif "Lower" in response:
        high = guess - 1

s.close()
