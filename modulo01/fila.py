# Exemplo de implementação de uma fila usando deque do módulo collections em Python
# A fila é uma estrutura de dados do tipo FIFO (First In, First Out), onde
# o primeiro elemento adicionado é o primeiro a ser removido.
# Neste exemplo, utilizamos a classe deque do módulo collections para representar a fila, onde o
from collections import deque # Importa a classe deque do módulo collections para criar uma fila eficiente
fila = deque()
fila.append('A')
fila.append('B') 
fila.append('C')
print(fila)  # Imprime a fila completa
fila.popleft()  # Remove o primeiro elemento da fila (A)
print(fila)  # Imprime a fila atualizada após a remoção do primeiro elementos