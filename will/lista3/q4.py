n = int(input('Digite um número (0 para encerrar): '))

while n != 0: 
    multiplo = n

    while multiplo < 100:
        print(multiplo)
        multiplo += n 
    print('----')
    n = int(input('Digite outro número (0 para encerrar): '))
    