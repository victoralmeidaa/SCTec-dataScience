import pandas as pd

data = {
    'nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'endereco': ['Rua A', 'Rua B', 'Rua C', 'Rua D', 'Rua E'],
    'data de Nascimento': ['1990-01-01', '1985-05-15', '1992-07-20', '1988-12-10', '1995-03-25'],
    'data de admissao': ['2020-01-01', '2019-05-15', '2021-07-20', '2018-12-10', '2022-03-25'],
    'salario': [5000, 6000, 5500, 7000, 6500],
    'cargo': ['Analista', 'Desenvolvedor', 'Analista', 'Gerente', 'Desenvolvedor']
}

df = pd.DataFrame(data)
print(df)

print(df['data de admissao']) # acessando a coluna 'data de admissao'

