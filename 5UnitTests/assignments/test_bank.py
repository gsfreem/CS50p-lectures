from bank import value

def test_bank_letters():
    assert value('h') == 20
    assert value('H') == 20
    assert value('a') == 100
    assert value('A') == 100

def test_bank_words():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('hey') == 20
    assert value('Hey') == 20
    assert value('greetings') == 100
    assert value('Greetings') == 100

def test_bank_sentence():
    assert value('hello andy') == 0
    assert value('Hello andy') == 0
    assert value('hey andy') == 20
    assert value('Hey andy') == 20
    assert value('greetings andy') == 100
    assert value('Greetings andy') == 100