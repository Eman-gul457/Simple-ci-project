from app.app import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_neg_and_pos():
    assert add(-1, 1) == 0
