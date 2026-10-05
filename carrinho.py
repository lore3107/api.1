class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhosDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self, desconto_percentual=0):
        total = sum(produto.preco for produto in self.produtos)
        valor_desconto = total * (desconto_percentual / 100)
        return total - valor_desconto