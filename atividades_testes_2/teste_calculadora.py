import atividades_testes_2
from atividades_testes_2 import somar, multiplicar, subtrair

@atividades_testes_2.mark.basico
def test_somar():
    assert somar(5, 2) == 7

@atividades_testes_2.mark.basico
def test_multiplicar():
    assert multiplicar(3, 2) == 6

@atividades_testes_2.mark.avancado
def test_subtrair():
    assert subtrair(8, 4) == 4
