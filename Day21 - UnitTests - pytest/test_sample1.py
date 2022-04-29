def func(x):
    return x + 2

def test_answer():
    assert func(3) == 5

def test_myName():
    name = 'Hello'
    txt = 'Hello World'
    assert name in txt

def test_3():
    name = 'Hedllo'
    txt = 'Hello World'
    assert name in txt, 'name not found'