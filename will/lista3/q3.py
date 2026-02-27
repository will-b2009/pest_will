soma = 0
quantidade = 0

n = int(input('Digite um número (-1 parar): '))

while n != -1: 
    soma += n 
    quantidade += 1
    n = int(input('Digite um número (-1 para parar): '))

if quantidade > 0:
    media = soma / quantidade 
    print('Média:', media)
else:
    print('Nenhum número válido foi digitado.')
    
