contador = 1 

while contador <= 50:
    if contador % 4 == 0 and contador % 6 == 0:
        print('QuadHex')
    elif contador % 4 == 0:
        print('Quad')
    elif contador % 6 == 0: 
        print('Hex')
    else:
        print(contador)

    contador += 1 
    