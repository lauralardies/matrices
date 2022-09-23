def lista(inicio, fin):
    return list(range(inicio, fin + 1))

def pares(incio, fin):
    return list(range(incio, fin + 1, 2))

def impares(inicio, fin):
    return list(range(inicio + 1, fin + 1, 2))

def multiplo(inicio, fin, n):
    return [i for i in range(len(lista(inicio, fin))) if i%n == 0]