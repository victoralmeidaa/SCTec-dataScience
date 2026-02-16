num_init  = int(input('Digite um valor inicial: '))
num_final  = int(input('Digite um valor final: '))

for num in range(num_init, num_final + 1):
    if num % 2 == 0:
        print(num)
    
        