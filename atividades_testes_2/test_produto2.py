import atividades_testes_2
from conftest import configuracao

def test_ambiente_produto(configuracao):
    assert configuracao["ambiente"] == "teste"
    