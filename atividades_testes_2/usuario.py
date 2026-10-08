import atividades_testes_2

@atividades_testes_2.fixture(scope="module")
def usuario():
    print("\nCriando usuário")
    return {
        "nome": "Lorena",
        "idade": 17, 
    }
