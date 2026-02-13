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