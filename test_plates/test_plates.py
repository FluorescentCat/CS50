from plates import is_valid

def test_length():
    assert is_valid("AAA222") == True
    assert is_valid("A") != True

def test_specialchar():
    assert is_valid("AA23.5") != True

def test_firsttwo():
    assert is_valid("A12345") != True

def test_nummiddle():
    assert is_valid("AAA22A") != True

def test_zero():
    assert is_valid("AA02") != True
    assert is_valid("AA20") == True

def main():
    test_length()
    test_specialchar()
    test_firsttwo()
    test_nummiddle()
    test_zero()

if __name__ == "__main__":
    main()