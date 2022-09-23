def suma(matriz):
    for n in range(0, len(matriz)):
        matriz[n][-1] = sum(matriz[n][:-1])
    return matriz