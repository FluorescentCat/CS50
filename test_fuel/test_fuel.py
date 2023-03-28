from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zeroError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        
def test_valueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def main():
    test_convert()
    test_gauge()
    test_zeroError()
    test_valueError()

if __name__ == "__main__":
    main()