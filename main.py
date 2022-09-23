from ejercicio1 import suma
from ejercicio2 import condicion
from ejercicio3 import lista_recursiva
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

print(lista_recursiva(0, 10, 1, 1))
print(lista_recursiva(-10, 0, 1, 1))
print(lista_recursiva(0, 20, 1, 2))
print(lista_recursiva(-19, 0, 1, 2))
print(lista_recursiva(0, 50, 1, 5))

print("-----------------------------------------------")
print("----------------- EJERCICIO 4 -----------------")
print("-----------------------------------------------")

n = int(input("Introduzca el número de filas de su tabla: "))
m = int(input("Introduzca el número de columnas de su tabla: "))

if __name__ == '__main__':
    main(n, m)
