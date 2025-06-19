from add import add
# funcion add
def test_add():
    assert add(2, 3) == 5
    # assert add(-1, 1) == 10 # descomentar para tener resultados
    assert add(-1, 1) == 0
    assert add(0, 0) == 10
    assert add(10, 20) == 30

# test_add() # solo para pruebas
