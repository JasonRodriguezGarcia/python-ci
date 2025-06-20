from mathematics import add, multiply

# funcion add
def test_add():
    assert add(2, 3) == 5
    # assert add(-1, 1) == 10 # descomentar para tener resultados
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, 20) == 30

# test_add() # solo para pruebas
def test_multiply():
    assert multiply(2, 3) == 6
    # assert multiply(-1, 1) == 10 # descomentar para tener resultados
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
    assert multiply(10, 10) == 100

test_multiply()
test_add()