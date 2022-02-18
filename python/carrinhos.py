import sys

class Carrinho:
    def __init__(self, preco: float, quantidade: int, id_produto: int):
        self.id_produto = id_produto
        self.preco = preco
        self.quantidade = quantidade

def ler_carrinhos() -> list[Carrinho]:
    produtos: list[Carrinho] = []
    for line in sys.stdin:
        preco, quantidade = line.split('\t')
        produtos.append(Carrinho(float(preco), int(quantidade), None))
            
    return produtos