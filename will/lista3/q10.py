inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

n = inicio

while n <= fim:
    soma = 0 
    divisor = 1

    while divisor < n:
        if n % divisor == 0:
            soma += divisor 
        divisor += 1 
    if soma == n and n != 0:
        print(n, 'é um número perfeito.')

    n += 1 
    