phone = ['11111-1111', '22222-2222', '33333-3333', '44444-4444', '55555-5555']

print(phone)  # Imprime a lista completa de números de telefone
print(phone[0])  # Acessa o primeiro elemento da lista
print(phone[1])  # Acessa o segundo elemento da lista

phone.append('66666-6666')  # Adiciona um novo número à lista
print(phone)  # Imprime a lista atualizada com o novo número

phone.insert(0, '00000-0000')  # Insere um número no início da lista
print(phone)  # Imprime a lista atualizada com o número inserido no início

phone.remove('33333-3333')  # Remove um número específico da lista
print(phone)  # Imprime a lista atualizada após a remoção do número
phone.pop(2)  # Remove o número no índice 2 (terceiro elemento)
print(phone)  # Imprime a lista atualizada após a remoção do número no índice 2

contato = ('João', '11111-1111')

phone02 = []
phone02.append(contato)
print(phone02)  # Imprime a lista phone02, que está vazia

phone03 = [('João', '11111-1111'), ('Maria', '22222-2222'), ('Pedro', '33333-3333')]
print(phone03)  # Imprime a lista phone03, que contém três tuplas, cada uma representando um contato com nome e número de telefone

print(phone03[0],phone03[2])  # Acessa o primeiro e terceiro elementos da lista phone03

phone03_dict = dict(phone03)  # Converte a lista de tuplas em um único dicionário
print(phone03_dict)  # Imprime o dicionário resultante da conversão
print(phone03_dict['João'])  # Acessa o número de telefone associado ao nome 'João' no dicionário phone03_dict

phone03_dict['Ana'] = '44444-4444'  # Adiciona um novo contato ao dicionário phone03_dict
print(phone03_dict)  # Imprime o dicionário atualizado com o novo contato 'Ana' e seu número de telefone

phone03_dict.pop('Pedro')  # Remove o contato 'Pedro' do dicionário phone03_dict
print(phone03_dict)  # Imprime o dicionário atualizado após a remoção do contato 'Pedro'