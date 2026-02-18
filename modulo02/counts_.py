import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

survived_counts = df['survived'].value_counts()

print(survived_counts)

plt.figure(figsize=(8,5))
plt.bar(survived_counts.index, survived_counts)
plt.title('Contagem Sobrevivente')
plt.xlabel('Sobrevivente 0/1')
plt.ylabel('Contagem')
plt.show()