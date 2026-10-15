import pytest

@pytest.fixture(scope="session")
# Cria a fixture uma única vez durante a sessão de testes
def configuracao():
    print("\nCarregando configuração")
    return {"ambiente": "teste"}
    
