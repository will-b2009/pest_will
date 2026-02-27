n = int(input('Digite um número: '))

soma = 0 
contador = 1 

while contador < n: 
    if n % contador == 0:
        soma += contador 
    contador += 1 

if soma ==  n:
    print('É um número perfeito: ')
else:
    print('Não é um número perfeito' )
