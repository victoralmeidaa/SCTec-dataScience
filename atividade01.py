try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Por favor, digite um número válido.")
    exit()

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
        exit()

resultado = dividir(num1, num2)
print(f"O resultado da divisão é: {resultado}")
