# ggame/game.py

import random

def generate_random(difficulty):
    if difficulty == 1:
        return random.randint(1, 10)
    elif difficulty == 2:
        return random.randint(1, 50)
    return random.randint(1, 100)

def get_difficulty(c):
    prompt = """
    Difficulty
    ==========
    1) easy
    2) medium 
    3) hard
    enter choice:"""
    c.sendall(prompt.encode())
    return int(c.recv(1024).decode().strip())

def check_guess(user_guess, correct_answer):
    if user_guess == correct_answer:
        return "correct"
    elif user_guess > correct_answer:
        return "lower"
    return "higher"
