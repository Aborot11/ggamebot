import pytest
from unittest.mock import MagicMock
import bot_client

def test_connect_to_server(monkeypatch):
    mock_sock = MagicMock()
    monkeypatch.setattr(bot_client.socket, 'socket', lambda *args, **kwargs: mock_sock)
    result = bot_client.connect_to_server('localhost', 7777)
    assert result is mock_sock
    mock_sock.connect.assert_called_once_with(('localhost', 7777))

def test_select_difficulty():
    mock_sock = MagicMock()
    mock_sock.recv.return_value = b"Select difficulty (1: Easy, 2: Medium, 3: Hard)"
    diff = bot_client.select_difficulty(mock_sock)
    mock_sock.sendall.assert_called_once_with(b'3')
    assert diff == '3'

def test_get_banner():
    mock_sock = MagicMock()
    mock_sock.recv.return_value = b"===WELCOME==="
    banner = bot_client.get_banner(mock_sock)
    assert banner == '===WELCOME==='

def test_make_guess_easy():
    guess = bot_client.make_guess('1')
    assert 1 <= guess <= 10

def test_make_guess_medium():
    guess = bot_client.make_guess('2')
    assert 1 <= guess <= 50

def test_make_guess_hard():
    guess = bot_client.make_guess('3')
    assert 1 <= guess <= 100

def test_send_guess_and_receive_response():
    mock_sock = MagicMock()

    mock_sock.recv.return_value = b"CORRECT!"
    response = bot_client.send_guess_and_receive_response(mock_sock, 42)
    mock_sock.sendall.assert_called_with(b'42')
    assert response == 'CORRECT!'

    mock_sock.recv.return_value = b"Higher"
    response = bot_client.send_guess_and_receive_response(mock_sock, 10)
    assert response == 'Higher'

    mock_sock.recv.return_value = b"Lower"
    response = bot_client.send_guess_and_receive_response(mock_sock, 90)
    assert response == 'Lower'
