from kannada import knutils


def test_letters():
    assert knutils.letters("ನನ್ನಂತೆ") == ["ನ", "ನ್ನಂ", "ತೆ"]
