n = int(input('Digite um número: '))

fatorial = 1 
contador = n 

while contador > 1:
    fatorial *= contador 
    contador -= 1 

print('Fatorial =', fatorial)


