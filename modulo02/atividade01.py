import pandas as pd

df = pd.read_csv('IceCreamSales-temperatures.csv')

print(df.sort_values(by='Temperature', ascending=False).head(10)) # Ordenou os dados em ordem decrecente
