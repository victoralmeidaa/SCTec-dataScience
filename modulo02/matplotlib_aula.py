import matplotlib.pyplot as plt
import numpy as np

x = ['maça', 'banana', 'laranja', 'uva', 'abacaxi']
y = [10, 15, 7, 12, 5]

plt.bar(x, y)

plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()

# Atividade: crie dois arrays com nomes e salários de funcionarios; 
# em seguida, mostre na tela o grafico destes valores;

array_funcionarios = np.array(['João', 'Maria', 'Pedro', 'Ana', 'Carlos'])
array_salarios = np.array([3000, 3500, 4000, 3200, 4500])
plt.bar(array_funcionarios, array_salarios)
plt.xlabel('Funcionários')
plt.ylabel('Salários')
plt.title('Salários dos Funcionários')
plt.show()

# grafico de scatter
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.scatter(x, y, marker='*', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersão')
plt.show()