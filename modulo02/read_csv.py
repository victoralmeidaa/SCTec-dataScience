import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')

print(df.head()) # exibe as primeiras 5 linhas do DataFrame para ter uma visão geral dos dados

print(df.info()) # informações sobre o DataFrame, incluindo o número de entradas, colunas, tipos de dados e valores nulos

print(df.describe()) #  estatísticas descritivas para colunas numéricas

print(df.dtypes) # datatypes de cada coluna

print(df[df['age'] <= 10].head()) # exibe as primeiras 5 linhas do DataFrame onde a idade dos passageiros é menor que 10 anos

duplicateRows = df[df.duplicated()] # identifica linhas duplicadas no DataFrame
print(duplicateRows) # exibe as linhas duplicadas, se houver   
print(len(duplicateRows)) # exibe o número de linhas duplicadas, se houver

df.drop_duplicates(keep='last', inplace=True) # remove as linhas duplicadas, mantendo a última ocorrência
print(len(df)) # exibe o número de linhas restantes após a remoção de duplicatas

df.dropna(subset=['deck'], inplace=True) # remove as linhas onde a coluna 'deck' tem valores nulos
print(df) # exibe o número de linhas restantes após a remoção de linhas com

df = df.rename(columns={'sex': 'Genero'}) # renomeia a coluna 'sex' para 'Genero'
print(df.head(5)) # exibe as primeiras 5 linhas do DataFrame para verificar a alteração

sorted_df = df.sort_values(by='Genero', ascending=False) # ordena o DataFrame pela coluna 'Genero' em ordem crescente
print(sorted_df)