# tests/test_ggame.py
import pytest
from ggame.game import generate_random, get_difficulty, check_guess

# 1. Test generate_random (for different difficulties)
def test_generate_random_easy():
    result = generate_random(1)
    assert 1 <= result <= 10, "The result should be between 1 and 10 for easy difficulty."

def test_generate_random_medium():
    result = generate_random(2)
    assert 1 <= result <= 50, "The result should be between 1 and 50 for medium difficulty."

def test_generate_random_hard():
    result = generate_random(3)
    assert 1 <= result <= 100, "The result should be between 1 and 100 for hard difficulty."


# 2. Test get_difficulty (mocking the socket interaction)
# For this, we will mock the socket and simulate what it would return for a difficulty choice.

from unittest.mock import MagicMock

def test_get_difficulty():
    # Create a mock socket
    mock_socket = MagicMock()
    mock_socket.recv.return_value = b'2'  # Simulate the client sending '2' (medium difficulty)

    difficulty = get_difficulty(mock_socket)
    assert difficulty == 2, "The difficulty should be medium (2)."

# 3. Test check_guess function
def test_check_guess_correct():
    result = check_guess(5, 5)
    assert result == "correct", "The result should be 'correct' when the guess is correct."

def test_check_guess_lower():
    result = check_guess(3, 5)
    assert result == "higher", "The result should be 'higher' when the guess is too low."

def test_check_guess_higher():
    result = check_guess(7, 5)
    assert result == "lower", "The result should be 'lower' when the guess is too high."
