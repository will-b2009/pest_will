n = int(input('Digite um número: '))
soma = 0 
pass
for i in range(1, n):
    if i % 4 == 0 or i % 6 == 0:
        soma += i
        pass
print(soma)    
