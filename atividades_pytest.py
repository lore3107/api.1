# função de soma
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(10, 5) == 15
    assert soma(-2, 5) == 3





# função que verifica se o nome é igual ao esperado
def verificar_nome(nome):
    return nome 

def test_verificar_nome():
    assert verificar_nome("Lorena") == "Lorena"
    assert verificar_nome("João") == "João"
    assert verificar_nome("Maria") == "Maria"





# função que verifica se a idade é maior ou menor de idade
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def test_verificar_idade():
    assert verificar_idade(20) == "Maior de idade"
    assert verificar_idade(12) == "Menor de idade"
    assert verificar_idade(27) == "Maior de idade"





# função de divisão
def dividir(a, b):
    return a / b

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(20, 4) == 5
    assert dividir(15, 3) == 5

import atividades_pytest
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def test_divisao_por_zero():
    with atividades_pytest.raises(ValueError) as error_info:
        dividir(10, 0)

    assert str(error_info.value) == "Não é possível dividir por zero"




# função de divisão normal e com tratamento de exceção
def test_divisao_normal():
    assert dividir(10, 2)  == 5

def test_divisao_por_zero():
    with atividades_pytest.raises(ValueError):
        dividir(10, 0)

def test_mensagem_erro():
    with atividades_pytest.raises(ValueError) as error_info:
        dividir(10, 0)
    assert str(error_info.value) == "Não é possível dividir por zero"





# função que retorna um dicionário com informações do usuário
def obter_usuario():
    return {
        "nome": "Lorena",
        "idade": 25,
        "ativo": True
    }
def test_obter_usuario():
    assert isinstance(obter_usuario(), dict)
    assert obter_usuario()["nome"] == "Lorena"
    assert isinstance(obter_usuario()["idade"], int)
    assert obter_usuario()["ativo"] == True





# função que verifica se o usuário pode entrar
def verificar_usuario(usuario):
    if usuario["idade"] >= 18:
        return "Pode entrar"
    else:
        return "Não pode entrar"
def test_verificar_usuario():
    assert verificar_usuario({"nome": "Lorena", "idade": 20}) == "Pode entrar"
    assert verificar_usuario({"nome": "Maria", "idade": 18}) == "Pode entrar"
    assert verificar_usuario({"nome": "João", "idade": 15}) == "Não pode entrar"





# função de multiplicação com teste parametrizado
def multiplicar(a, b):
    return a * b
def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 4) == 20
    assert multiplicar(10, 2) == 20
    assert multiplicar(7, 0) == 0
@atividades_pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (5, 4, 20),
    (10, 2, 20),
    (7, 0, 0)
])





# função de multiplicação com diferentes valores de entrada usando parametrize
def multiplicar(a, b):
    return a * b
def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 4) == 20
    assert multiplicar(10, 2) == 20
    assert multiplicar(7, 0) == 0
@atividades_pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (5, 4, 20),
    (10, 2, 20),
    (7, 0, 0)
])
def test_multiplicar(a, b, resultado):
    # testa a função multiplicar com diferentes valores de entrada
    assert multiplicar(a, b) == resultado





# função de desconto
def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)
@atividades_pytest.mark.parametrize("preco, desconto, resultado", [
    (100, 10, 90),
    (200, 20, 160),
    (50, 10, 45)
])
def test_calcular_desconto(preco, desconto, resultado):
    assert calcular_desconto(preco, desconto) == resultado
def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)
@atividades_pytest.mark.parametrize("preco, desconto, resultado", [
    (100, 10, 90),
    (200, 20, 160),
    (50, 10, 45)
])
def test_calcular_desconto(preco, desconto, resultado):
    assert calcular_desconto(preco, desconto) == resultado





# função de média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
def test_calcular_media():
    assert calcular_media(8, 6) == 7





# função de desconto
def buscar_desconto():
    return 10
def calcular_preco(preco):
    desconto = buscar_desconto()
    return preco - (preco * desconto / 100)
def test_calcular_preco():
    assert calcular_preco(200) == 180
    assert calcular_preco(100) == 90
    assert calcular_preco(50) == 45





# mocker
def test_calcular_preco_com_mock(mocker):
    mocker.patch("tests.run.buscar_desconto", return_value=20)
    assert calcular_preco(100) == 80
    # mocker.patch substitui temporariamente o comportamento de alguma função durante o teste

def test_buscar_desconto_foi_chamada(mocker):
    mocker.patch("tests.run.buscar_desconto", return_value=20)
    calcular_preco(100)
    assert mocker.called
    # called - a função foi chamada?

def test_buscar_desconto_foi_chamada_duas_vezes(mocker):
    mock = mocker.patch("tests.run.buscar_desconto", return_value=20)
    calcular_preco(100)
    calcular_preco(200)
    assert mock.call_count == 2
    # call_count - a função foi chamada quantas vezes?

def buscar_desconto(cliente_id):
    return 10
def calcular_preco(preco, cliente_id):
    desconto = buscar_desconto(cliente_id)
    return preco - (preco * desconto / 100)
def test_calcular_preco_com_mock(mocker):
    mocker.patch("tests.run.buscar_desconto", return_value=20)
    assert calcular_preco(100, 42) == 80
    mocker.assert_called_once_with(42)
    # assert_called_once_with - a função foi chamada uma vez com o valor 42?

def buscar_desconto(cliente_id):
    return 10
def calcular_preco(preco, cliente_id):
    desconto = buscar_desconto(cliente_id)
    return preco - (preco * desconto / 100)





# side_effect - permite especificar diferentes valores de retorno para cada chamada da função mockada
def test_descontos_diferentes(mocker):
    mocker.patch("tests.run.buscar_desconto", side_effect=[10,20, 30])
    assert calcular_preco(10) == 9
    assert calcular_preco(20) == 16
    assert calcular_preco(30) == 21

def desconto_por_cliente(cliente_id):
    if cliente_id == 1:
        return 10
    elif cliente_id == 2:
        return 20
    elif cliente_id == 3:
        return 30
def test_descontos_por_cliente(mocker):
    mocker.patch("tests.run.buscar_desconto", side_effect = desconto_por_cliente)
    assert calcular_preco(100, 2) == 80

def test_descontos_por_cliente(mocker):
    mocker.patch("tests.run.buscar_desconto", side_effect = desconto_por_cliente)
    assert calcular_preco(100, 1) == 90
    assert calcular_preco(100, 2) == 80
    assert calcular_preco(100, 3) == 70





# parametrize - permite executar o mesmo teste com diferentes valores de entrada 


