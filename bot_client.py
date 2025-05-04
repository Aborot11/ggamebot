import socket

# Connect to the server
# Returns a socket object (mockable in tests)
def connect_to_server(host, port):
    s = socket.socket()
    s.connect((host, port))
    return s

# Select difficulty: reads prompt, sends choice, returns choice
# For now, selects "3" by default (Hard)
def select_difficulty(s):
    prompt = s.recv(1024).decode().strip()
    print(f"[SERVER] {prompt}")

    difficulty = "3"  # Change to "1" or "2" for other levels
    difficulty_map = {"1": "Easy (1–10)", "2": "Medium (1–50)", "3": "Hard (1–100)"}
    print(f"[BOT] Selected Difficulty: {difficulty_map[difficulty]}")
    s.sendall(difficulty.encode())
    return difficulty

# Receive and return the game banner from server
def get_banner(s):
    banner = s.recv(1024).decode().strip()
    print(f"[SERVER] {banner}")
    return banner

# Generate a guess based on difficulty
# Uses midpoint strategy
def make_guess(difficulty):
    if difficulty == "1":
        low, high = 1, 10
    elif difficulty == "2":
        low, high = 1, 50
    else:
        low, high = 1, 100
    return (low + high) // 2

# Send guess to server and return decoded response
def send_guess_and_receive_response(s, guess):
    s.sendall(str(guess).encode())
    response = s.recv(1024).decode().strip()
    print(f"[SERVER] {response}")
    return response

# Main bot client loop (for manual execution)
def bot_client(host='localhost', port=7777):
    s = connect_to_server(host, port)
    difficulty = select_difficulty(s)
    get_banner(s)

    low, high = 1, 100
    if difficulty == "1":
        high = 10
    elif difficulty == "2":
        high = 50

    while True:
        guess = (low + high) // 2
        print(f"[BOT] Guessing: {guess}")
        response = send_guess_and_receive_response(s, guess)
        if "CORRECT!" in response:
            print(f"[BOT] Correct Guess: {guess}")
            break
        elif "Higher" in response:
            low = guess + 1
        elif "Lower" in response:
            high = guess - 1
    s.close()
