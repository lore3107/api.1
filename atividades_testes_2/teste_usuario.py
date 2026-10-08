def test_nome_usuario(usuario):
    assert usuario["nome"] == "Lorena"

def test_idade_usuario(usuario):
    assert usuario["idade"] == 17