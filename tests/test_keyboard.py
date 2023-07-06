from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    assert kb.name == "Dark Project KD87A"
    kb.change_lang()
    assert kb.language == "RU"
