from ejercicio1 import suma
from ejercicio2 import condicion
from ejercicio3 import lista, pares, impares, multiplo
from tabla import main

print("-----------------------------------------------")
print("----------------- EJERCICIO 1 -----------------")
print("-----------------------------------------------")

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 7],
    [4, 4, 4, 13]
]

print(suma(matriz))

print("-----------------------------------------------")
print("----------------- EJERCICIO 2 -----------------")
print("-----------------------------------------------")

str = input("Introduce la cadena que usted quiera: ")

print(condicion(str))

print("-----------------------------------------------")
print("----------------- EJERCICIO 3 -----------------")
print("-----------------------------------------------")

print(lista(0, 10))
print(lista(-10, 0))
print(pares(0, 20))
print(impares(-20, 0))
print(multiplo(0, 50))

print("-----------------------------------------------")
print("----------------- EJERCICIO 4 -----------------")
print("-----------------------------------------------")

n = int(input("Introduzca el número de filas de su tabla: "))
m = int(input("Introduzca el número de columnas de su tabla: "))

if __name__ == '__main__':
    main(n, m)
