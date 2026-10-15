import atividades_testes_2
from atividades_testes_2.conftest import configuracao

def test_ambiente(configuracao):
    assert configuracao["ambiente"] == "teste"