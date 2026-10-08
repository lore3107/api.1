import atividades_testes_2
from login import login

def test_login_correto():
    assert login("lorena", "1234") == True

@atividades_testes_2.mark.skip
# nem executa: skip
def test_login_errado():
    assert login("lorena", "154") == False

@atividades_testes_2.mark.xfail
# executa, mas esperamos que falhe: xfail
def test_login_invalido():
    assert login("email", "1234") == True