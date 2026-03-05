n = int(input('Digite um número: '))
soma = 0
pass
for i in range(1, n):
    if n % i == 0:
        soma = soma + i
        pass
if soma == n:
    print('Número perfeito')
else:
    print('Não é perfeito')
    