from twttr import shorten

def test_shorten():
    assert shorten('greg') == 'grg'
    assert shorten('9') == '9'
    assert shorten('grEg') == 'grg'
    assert shorten('grg,') == 'grg,'
    