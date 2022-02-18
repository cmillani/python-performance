# Comparação de cálculos em linguagens

Nesse repositório vamos explorar (com um cenários bem específico) como um cálculo simples em uma massa de dados é afetado pela linguagem de programação e frameworks utilizados.
Os dados expostos aqui não são uma regra :) mas expõem um cenário que esbarramos no produto onde atuo na AmbevTech, onde usamos Pandas para algumas operações no backend.

Para executar os comandos abaixo você deve ter instalado as seguintes ferramentas:

* python
* gcc
* dotnet

Os exemplos de comando foram executados em um _shell bash_.

# Setup do ambiente

Primeiro, vamos gerar os dados!
Basta rodar:
```sh 
python gerar_dados.py > dados.txt
```

## C

Entre na pasta `c` e execute:

```sh
gcc main.c -o main.o
./main.o < ../dados.txt
```

## DotNet

Entre na pasta `dotnet/App` e execute:
```
dotnet run < ../../dados.txt
```

## Python

Entre na pasta `python` e execute:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python calculo_loop.py < ../dados.txt
python calculo_pandas.py < ../dados.txt
```

