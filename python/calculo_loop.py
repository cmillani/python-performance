from carrinhos import Carrinho, ler_carrinhos
import time

def get_ticket_medio(carrinhos: list[Carrinho]):
    total = 0
    for carrinho in carrinhos:
        total += carrinho.preco * carrinho.quantidade
    return total/len(carrinhos)


carrinhos = ler_carrinhos()

t0 = time.time()
media = get_ticket_medio(carrinhos)
t1 = time.time()

print(f'Tempo Calculo: {t1 - t0}s')
print(media)