import numpy as np
array1 = np.array([10, 20, 30, 40, 50])
print(array1)
print(array1[0]) # acessando o primeiro elemento do array
print(array1[1:4]) # acessando os elementos do índice 1 ao 3 do array

array2 = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

print(array2)
print(array2[0, 0]) # acessando o elemento da primeira linha e primeira coluna do array
print(array2[1, 2]) # acessando o elemento da segunda linha e terceira coluna do array

print(f'Shape do array1: {array1.shape}') # shape retorna a dimensão do array
print(f'Shape do array2: {array2.shape}') # shape retorna a dimensão do array   

print(f'size do array1: {array1.size}') # size retorna o número total de elementos do array
print(f'size do array2: {array2.size}') # size retorna o número total

print('media do array1:', np.mean(array1)) # média dos elementos do array
print('media do array2:', np.mean(array2)) # média dos elementos do array

print('desvio padrão do array1:', np.std(array1)) # desvio padrão dos elementos do array
print('desvio padrão do array2:', np.std(array2)) # desvio padrão dos elementos do array

# atividade 01 - Crie um array com alguns valores inteiros e calcule a media.

array3 = np.array([5, 10, 15, 20, 40])
print(array3)
print('media do array3:', np.mean(array3))