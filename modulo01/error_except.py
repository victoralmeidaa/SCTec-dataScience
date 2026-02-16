try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Por favor, digite um número válido.")
    exit()

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    finally:
        print("Operação de divisão concluída.")

print(dividir(num1, num2))
    

