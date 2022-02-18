import time
from carrinhos import Carrinho, ler_carrinhos
import pandas as pd

def mapeia_produto_dataframe(carrinhos: list[Carrinho]) -> pd.DataFrame:
    return pd.DataFrame.from_records([produto.__dict__ for produto in carrinhos])

def get_ticket_medio(df_produto: pd.DataFrame) -> float:
    total = df_produto['preco'] * df_produto['quantidade']

    return total.mean()
    
carrinhos = ler_carrinhos()

t0 = time.time()
df = mapeia_produto_dataframe(carrinhos)
t1 = time.time()
media = get_ticket_medio(df)
t2 = time.time()

print(f'Tempo Map: {t1 - t0}s\nTempo Calculo:{t2 - t1}s')
print(media)