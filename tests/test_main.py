from main import soma, subtrai, multiplica, divide, eh_par

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_multiplica():
    assert multiplica(4, 2) == 8

def test_divide():
    assert divide(10, 2) == 5

def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(5) is False


