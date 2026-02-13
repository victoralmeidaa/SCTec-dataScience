# Exemplo de implementação de uma pilha usando uma lista em Python
# A pilha é uma estrutura de dados do tipo LIFO (Last In, First Out), onde o último elemento adicionado é o primeiro a ser removido.
# Neste exemplo, utilizamos uma lista para representar a pilha, onde o método append() é usado para adicionar elementos ao topo da pilha e o método pop() é usado para remover o elemento do topo da pilha.
pilha = []
pilha.append(1)
pilha.append(2)
pilha.append(3)
print(pilha)  # Imprime a pilha completas
pilha.pop()  # Remove o último elemento da pilha (3)
print(pilha)  # Imprime a pilha atualizada após a remoção do último