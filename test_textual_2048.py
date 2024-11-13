from game2048 import textual_2048
import pytest

def mock_input_return(obj):
    return obj

def test_read_player_command(monkeypatch): 
    for c in {"g","d","h","b"}:  
        monkeypatch.setattr(textual_2048, "read_player_command", lambda: mock_input_return(c))
        result = textual_2048.read_player_command()
        assert result == c