import pandas as pd

df = pd.read_csv('IceCreamSales-temperatures.csv')


print(df.info) # 

print(df.head())

print(df.sort_values(by='Temperature', ascending=False).head())

print(df.dtypes)

print(df['Temperature'])