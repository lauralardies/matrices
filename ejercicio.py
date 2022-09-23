# -----------------------------------------------
# ----------------- EJERCICIO 1 -----------------
# -----------------------------------------------

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
    return matriz
    
#print(suma(matriz))

# -----------------------------------------------
# ----------------- EJERCICIO 2 -----------------
# -----------------------------------------------

#str = input("Introduce la cadena que usted quiera: ")

def longitud(str):
	contador = 0
	for i in str:
		contador += 1
	return contador

def condicion(str):
    if longitud(str) >= 3 and longitud(str) < 10:
        print("El texto introducido por el usuario tiene longitud mayor o igual que tres y es menor que 10.")
    else:
        print("El texto introducido por el usuario NO tiene longitud mayor o igual que tres ni es menor que 10.")

#condicion(str)

# -----------------------------------------------
# ----------------- EJERCICIO 3 -----------------
# -----------------------------------------------

def lista(inicio, fin):
    return list(range(inicio, fin + 1))

def pares(incio, fin):
    return list(range(incio, fin + 1, 2))

def impares(inicio, fin):
    return list(range(inicio + 1, fin + 1, 2))

def multiplo(inicio, fin, n):
    return [i for i in range(len(lista(inicio, fin))) if i%n == 0]


print(lista(0, 10))
print(lista(-10, 0))
print(pares(0, 20))
print(impares(-20, 0))
print(multiplo(0, 50, 5))