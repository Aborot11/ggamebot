# simple_server.py

import socket
from ggame.game import generate_random, get_difficulty, check_guess

host, port = 'localhost', 12345
banner = b"\n====GUESSING GAME===\nenter guess:"

s = socket.socket()
s.bind((host, port))
s.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    conn, addr = s.accept()
    difficulty = get_difficulty(conn)
    answer = generate_random(difficulty)
    conn.sendall(banner)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        guess = int(data.decode().strip())
        res = check_guess(guess, answer)
        if res == "correct":
            conn.sendall(b"CORRECT!")
            break
        elif res == "lower":
            conn.sendall(b"=Guess Lower\nenter guess: ")
        else:
            conn.sendall(b"=Guess Higher\nenter guess: ")
    conn.close()
