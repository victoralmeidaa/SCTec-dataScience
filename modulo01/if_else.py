# Exemplo 1: If simples
idade = 18
if idade >= 18:
    print("Você é maior de idade")

# Exemplo 2: If/Else
temperatura = 15
if temperatura > 20:
    print("Está quente")
else:
    print("Está frio")

# Exemplo 3: If/Elif/Else
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Satisfatório")
else:
    print("Insuficiente")

# Exemplo 4: Condições com operadores lógicos
idade = 25
carteira = True
if idade >= 18 and carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# Aula 09
hora = 9
humor = 'sono'

if humor == 'sono' and hora < 10: # se o humor for sono e a hora for menor que 10, então cafezinho
    print('cafezinho')
elif humor == 'sedento' or hora < 2: # se o humor for sedento ou a hora for menor que 2, então limonada
    print('limonada')
else: # se nenhuma das condições anteriores for verdadeira, então água
    print('agua')

