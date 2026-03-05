inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '  ))
pass
for n in range(inicio, fim + 1):
    soma = 0 
    qtd = len(str(n))
    pass
    for d in str(n):
        soma +=int(d) ** qtd 
    pass
    if soma == n:
        print(n)
        