import random 

numero_secreto = random.randint(10, 50)

palpite = int(input('Adivinhe o número entre 10 e 50: '))

while palpite != numero_secreto:
    if palpite < numero_secreto: 
        print('o número secreto é MAIOR.')
    else:
        print('o número secreto é MENOR.')
        