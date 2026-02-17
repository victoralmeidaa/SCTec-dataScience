import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

df_por_sexo = titanic.groupby('sex')['survived'].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=df_por_sexo, x='sex', y='survived')
plt.xlabel('Sexo')
plt.ylabel('Número de Sobreviventes')
plt.title('Número de Sobreviventes por Sexo')
plt.show()

# idades dos passageiros do titanic
plt.figure(figsize=(10, 6))
sns.histplot(data=titanic, x='age') 
plt.show()

# Data set de voos usando heatmap para mostrar a quantidade de passageiros por mês e ano
voos = sns.load_dataset('flights')

voos = voos.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(12, 6))
sns.heatmap(voos, annot=True, fmt='.0f')
plt.show()
