from carrinho import Produto, CarrinhosDeCompras


def test_calcular_total_sem_desconto():
    carrinho = CarrinhosDeCompras()

produto1 = Produto(nome="Notebook", preco=3000)
produto2 = Produto(nome="Teclado", preco=500)

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

total_carrinho = carrinho.calcular_total()
assert total_carrinho == 3500

def test_calcular_com_desconto():
    carrinho = CarrinhosDeCompras()
    
    produto1 = Produto(nome="Notebook", preco=3000)
    produto2 = Produto(nome="Teclado", preco=500)
    
    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)

total_carrinho = carrinho.calcular_total(desconto_percentual=20)

assert total_carrinho == 2800