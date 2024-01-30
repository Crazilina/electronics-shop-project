from src.keyboard import Keyboard


def test_initialization():
    kb = Keyboard("Test Keyboard", 1000, 10)
    assert kb.name == "Test Keyboard"
    assert kb.price == 1000
    assert kb.quantity == 10
    assert kb.language == "EN"


def test_change_language():
    kb = Keyboard("Test Keyboard", 1000, 10)
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"


def test_repr():
    kb = Keyboard("Test Keyboard", 1000, 10)
    assert repr(kb) == "Keyboard('Test Keyboard', 1000, 10, Language: EN)"
