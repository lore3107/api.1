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




# mark.parametrize - permite executar o mesmo teste com valores diferentes
def calcular_dobro(numero):
    return numero * 2

@atividades_pytest.mark.parametrize("numero, resultado", [
    (2, 4),
    (4, 8),
    (6, 12)
])
def test_calcular_dobro(numero, resultado):
    assert calcular_dobro(numero) == resultado


def calcular_area(largura, altura):
    return largura * altura 

@atividades_pytest.mark.parametrize("largura, altura, resultado", [
    (5, 2, 10),
    (3, 4, 12),
    (10, 5, 50)
])
def test_calcular_area(largura, altura, resultado):
    assert calcular_area(largura, altura) == resultado

def calcular_frete(distancia, valor_por_km):
    return distancia * valor_por_km

@atividades_pytest.mark.parametrize("distancia, valor_por_km, resultado", [
    (10, 2, 20),
    (25, 3, 75),
    (100, 1.5, 150)
])
def test_calcular_frete(distancia, valor_por_km, resultado):
    assert calcular_frete(distancia, valor_por_km) == resultado


def classificar_nota(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
@atividades_pytest.mark.parametrize("nota, resultado", [
    (9, "Aprovado"),
    (7, "Aprovado"),
    (5, "Reprovado"),
    (3, "Reprovado")
])
def test_classificar_nota(nota, resultado):
    assert classificar_nota(nota) == resultado
    assert classificar_nota(9) == "Aprovado"

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

@atividades_pytest.mark.parametrize("peso, altura, resultado", [
    (60, 1.70, 20.76),
    (70, 1.75, 22.85),
    (80, 1.80, 24.69)
])
def test_calcular_imc(peso, altura, resultado):
    assert round(calcular_imc(peso, altura), 2) == resultado

def verificar_email(email):
    return "@" in email
@atividades_pytest.mark.parametrize("email, resultado", [
    ("lorena@gmail.com", True),
    ("teste.com", False),
    ("abc@gmail.com", True),
    ("usuario", False)
])
def test_verificar_email(email, resultado):
    assert verificar_email(email) == resultado

def criar_produto():
    return {
        "nome": "Notebook",
        "preco": 3.000,
        "estoque": 10
    }
def test_criar_produto():
    assert isinstance(criar_produto()["nome"], str)
    assert criar_produto()["nome"] == "Notebook"
    assert isinstance(criar_produto()["preco"], float)
    assert criar_produto()["preco"] == 3.000
    assert isinstance(criar_produto()["estoque"]int)
    assert criar_produto()["estoque"] == 10

def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")

    return saldo - valor 

def test_saque_normal():
    assert sacar(100, 40) == 60
def test_saque_saldo_insuficiente():
    with atividades_pytest.raises(ValueError):
        assert sacar(100, 150)
def test_mensagem_erro():
    with atividades_pytest.raises(ValueError) as error_info:
        assert sacar(100, 150)
    assert str(error_info.value) == "Saldo insuficiente"


@atividades_pytest.fixture 
def produto():
    return {
        "nome": "Caderno", 
        "preco": 20
    }
def test_preco(produto):
    assert produto["preco"] == 20


import atividades_pytest 
@atividades_pytest.fixture 
def usuario():
    return {
        "nome": "Maria",
        "idade": 18
    }
def test_nome(usuario):
    assert usuario["nome"] == "Maria"
def test_idade(usuario):
    assert usuario["idade"] == 18


def calcular_total(preco, quantidade):
    return preco * quantidade
@atividades_pytest.fixture
def produto():
    return {
        "preco": 20, 
        "quantidade": 3
    }
def test_calcular_total(produto):
    assert calcular_total(
        produto["preco"],
        produto["quantidade"]
    ) == 60

@atividades_pytest.fixture
def produto():
    return {
        "nome": "Teclado",
        "preco": 80,
        "quantidade": 2
    }

def test_nome_produto(produto):
    assert produto["nome"] == "Teclado"

def test_total_produto(produto):
    assert calcular_total(
        produto["preco"],
        produto["quantidade"]
    ) == 160

def aplicar_desconto(preco, desconto):
    return preco - (preco * desconto / 100)
@atividades_pytest.fixture
def produto():
    return {
        "preco": 200,
        "desconto": 10
    }
def test_aplicar_desconto(produto):
    assert aplicar_desconto (
        produto["preco"],
        produto["desconto"]
    ) == 180


@atividades_pytest.mark.parametrize("desconto, resultado", [
    (10, 180),
    (20, 160)
])
def test_aplicar_desconto(produto, desconto, resultado):
    assert aplicar_desconto (
        produto["preco"],
        desconto
    ) == resultado


def aplicar_desconto(preco, desconto):
    if desconto < 0:
        raise ValueError("Desconto inválido")

    return preco - (preco * desconto / 100)

def test_desconto_invalido():
    with atividades_pytest.raises(ValueError) as error_info:
        aplicar_desconto(200, -10)

    assert str(error_info.value) == "Desconto inválido"



def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor
@atividades_pytest.mark.parametrize("valor, resultado", [
    (20, 80), 
    (50, 50)
])
def test_sacar(valor, resultado):
    assert sacar(
        100,
        valor
    ) == resultado


def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor
@atividades_pytest.mark.parametrize("saldo, valor", [
    (100, 150),
    (100, 200)
])
def test_saque_invalido(saldo, valor):
    with atividades_pytest.raises(ValueError) as error_info:
        sacar(saldo, valor)
    assert str(error_info.value) == "Saldo insuficiente" 



def calcular_frete(preco, distancia):
    if distancia <= 10:
        return 10
    elif distancia <= 30:
        return 20
    else: 
        return 30
@atividades_pytest.mark.parametrize("distancia, resultado", [
    (5, 10),
    (20, 20),
    (40, 30)
])
def test_calcular_frete(pedido, distancia, resultado):
    valor = calcular_frete(
        pedido["preco"],
        distancia
    )
    assert valor == resultado

def aplicar_desconto(preco, desconto):
    if desconto < 0:
        raise ValueError("Desconto inválido")
    return preco - (preco * desconto / 100)
def test_aplicar_desconto_inválido():
    with atividades_pytest.raises(ValueError) as error_info:
        aplicar_desconto(200, -10)
    assert str(error_info.value) == "Desconto inválido"

atividades_pytest.mark.parametrize("desconto", [
    -10,
    -20,
    -50
])
def test_aplicar_desconto_invalido(desconto):
    with atividades_pytest.raises(ValueError) as error_info:
# eu quero que essa função dê erro: with...
        aplicar_desconto(200, desconto)
    assert str(error_info.value) == "Desconto inválido"