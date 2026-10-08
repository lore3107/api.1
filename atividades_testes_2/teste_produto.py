import atividades_testes_2
from atividades_testes_2 import aplicar_desconto

@atividades_testes_2.fixture(params=[
    (100, 10, 90),
    (200, 20, 160),
    (300, 30, 210)
])
def dados_desconto(request):
    return request.param

def test_aplicar_desconto(dados_desconto):
    preco, percentual, resultado_esperado = dados_desconto
    resultado = aplicar_desconto(preco, percentual)
    assert resultado == resultado_esperado
