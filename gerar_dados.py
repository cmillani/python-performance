import random

tamanho_massa = 1000000

min_preco = 1
max_preco = 150

min_qtd = 1
max_qtd = 20

seed = 42
random.seed(seed)
for i in range(tamanho_massa):
    preco = random.uniform(min_preco, max_preco)
    quantidade = random.randint(min_qtd, max_qtd)
    print(f'{preco}\t{quantidade}')
