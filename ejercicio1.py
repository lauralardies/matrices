matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 7],
    [4, 4, 4, 13]
]

def suma(matriz):
    for j in matriz:
        del j[-1]
    for n in matriz:
        s = sum(n)
        if s != matriz[n][-1]:
            matriz[n][-1] = s
    print(matriz)
    
suma(matriz)