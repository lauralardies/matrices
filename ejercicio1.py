def suma(matriz):
    for j in matriz:
        del j[-1]
    for n in matriz:
        s = sum(n)
        if s != matriz[n][-1]:
            matriz[n][-1] = s
    return matriz