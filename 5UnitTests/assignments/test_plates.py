from plates import is_valid

def test_is_valid_1():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False

def test_is_valid_2():
    assert is_valid('PI3.14') == False
    assert is_valid('4PI3.1') == False

def test_is_valid_3():
    assert is_valid('H') == False
    
def test_is_valid_4():
    assert is_valid('OUTATIME') == False