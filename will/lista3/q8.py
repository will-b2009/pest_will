n = int(input('Digite um número decimal: '))

binario = ""

while n > 0:
    resto = n % 2 
    binario = str(resto) + binario 
    n = n // 2 

print('Binário:', binario)
