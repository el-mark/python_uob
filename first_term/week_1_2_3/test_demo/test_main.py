from main import add

def test_add():
    assert add(10, 10) == 20

def test_add_fails():
    assert add(10, 20) == 40
