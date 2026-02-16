def soma(): # Define a função soma que irá realizar a soma de dois números
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    return num1 + num2

# print(soma())  # Chama a função soma e imprime o resultado da soma dos dois números fornecidos pelo usuário

def pure_increment(elements,index): # Define a função pure_increment que recebe um número como argumento e retorna o número incrementado em 1
    new_elements = elements.copy() # Cria uma cópia da lista elements para evitar modificar a lista original
    new_elements[index] += 1 # Incrementa o elemento na posição index da lista new_elements em 1
    return new_elements # Retorna a nova lista modificada

lista = [1, 2, 3, 4, 5] # Define uma lista de números
print(pure_increment(lista,0)) # Chama a função pure_increment passando a lista e o índice 2, e imprime o resultado da lista modificada
print(lista) # Imprime a lista original para mostrar que ela foi modificada pela função pure_increment