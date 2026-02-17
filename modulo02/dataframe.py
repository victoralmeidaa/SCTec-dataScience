import pandas as pd

data = {
    'nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'idade': [30, 25, 35, 28],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df = pd.DataFrame(data)

print(df)

print(df['nome']) # acessando a coluna 'nome'

print(df.loc[0]) # acessando a primeira linha do DataFrame

print(df.loc[0, 'nome']) # acessando o nome da primeira linha do DataFrame
