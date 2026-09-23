def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(10, 5) == 15
    assert soma(-2, 5) == 3



    
def verificar_nome(nome):
    return nome 

def test_verificar_nome():
    assert verificar_nome("Lorena") == "Lorena"
    assert verificar_nome("João") == "João"
    assert verificar_nome("Maria") == "Maria"



def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def test_verificar_idade():
    assert verificar_idade(20) == "Maior de idade"
    assert verificar_idade(12) == "Menor de idade"
    assert verificar_idade(27) == "Maior de idade"



def dividir(a, b):
    return a / b

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(20, 4) == 5
    assert dividir(15, 3) == 5


import pytest
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def test_divisao_por_zero():
    with pytest.raises(ValueError) as error_info:
        dividir(10, 0)

    assert str(error_info.value) == "Não é possível dividir por zero"





def test_divisao_normal():
    assert dividir(10, 2)  == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_mensagem_erro():
    with pytest.raises(ValueError) as error_info:
        dividir(10, 0)
    assert str(error_info.value) == "Não é possível dividir por zero"


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


def verificar_usuario(usuario):
    if usuario["idade"] >= 18:
        return "Pode entrar"
    else:
        return "Não pode entrar"

def test_verificar_usuario():
    assert verificar_usuario({"nome": "Lorena", "idade": 20}) == "Pode entrar"
    assert verificar_usuario({"nome": "Maria", "idade": 18}) == "Pode entrar"
    assert verificar_usuario({"nome": "João", "idade": 15}) == "Não pode entrar"


def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 4) == 20
    assert multiplicar(10, 2) == 20
    assert multiplicar(7, 0) == 0

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (5, 4, 20),
    (10, 2, 20),
    (7, 0, 0)
])


# import pytest

def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 4) == 20
    assert multiplicar(10, 2) == 20
    assert multiplicar(7, 0) == 0


@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (5, 4, 20),
    (10, 2, 20),
    (7, 0, 0)
])
def test_multiplicar(a, b, resultado):
    # testa a função multiplicar com diferentes valores de entrada
    assert multiplicar(a, b) == resultado

    


def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)

@pytest.mark.parametrize("preco, desconto, resultado", [
    (100, 10, 90),
    (200, 20, 160),
    (50, 10, 45)
])
def test_calcular_desconto(preco, desconto, resultado):
    assert calcular_desconto(preco, desconto) == resultado

def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)

def test_calcular_desconto():
    # testa a função calcular_desconto com diferentes valores de entrada
    assert calcular_desconto(100, 5) == 95
    assert calcular_desconto(200, 10) == 180
    assert calcular_desconto(50, 10) == 45
    assert calcular_desconto(0, 20) == 0


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
def test_calcular_media():
    assert calcular_media(8, 6) == 7


def buscar_desconto():
    return 10

def calcular_preco(preco):
    return preco - (preco * desconto / 100)

def test_calcular_preco():
    assert calcular_preco(200) == 180
    assert calcular_preco(100) == 90
    assert calcular_preco(50) == 45

# mocker.patch substitui temporariamente o comportamento de alguma coisa durante o teste
def test_calular_preco_com_mock(mocker):
    mocker.patch("tests.run.buscar_desconto", return_value=20)
    assert calcular_preco(100) == 80
