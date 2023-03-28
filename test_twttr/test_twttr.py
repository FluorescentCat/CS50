from twttr import shorten

def test_novowels():
    assert shorten("world") == "wrld"
    assert shorten("Alice") == "lc"
    assert shorten("Crabby") == "Crbby"

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("!$?") == "!$?"

def main():
    test_novowels()
    test_numbers()
    test_punctuation()

if __name__ == "__main__":
    main()