cont = 0
pass
for n in range(1, 201):
    div = 0
    pass
    for i in range(1, n + 1):
        if n % i == 0:
            div += 1
            pass
    if div == 2:
        cont += 1
pass
print(cont)
 

