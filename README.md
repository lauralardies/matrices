# matrices

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/matrices)
https://github.com/lauralardies/matrices

## Ejercicio 1

La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

matriz = [[1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13]]

```
def suma(matriz):
    for n in range(0, len(matriz)):
        matriz[n][-1] = sum(matriz[n][:-1])
    return matriz
```

## Ejercicio 2

Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

```
def longitud(str) :
    if str == '':
        return 0
    else :
        return 1 + longitud(str[1:])

def condicion(str):
    if longitud(str) >= 3 and longitud(str) < 10:
        return True
    else:
        return False
```

## Ejercicio 3

Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

·        Todos los números del 0 al 10 [0, 1, 2, ..., 10]

·        Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

·        Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

·        Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

·        Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

## Ejercicio 4

Crea un script llamado tabla.py que realice las siguientes tareas:

·        Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.

·        El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.

·        En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.

·        El script contendrá un bucle for que itere el número de veces del primer argumento.

·        Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.

·        Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.

·        Ejecuta el código y observa el resultado.

·        Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.

```
def main(n, m):
    if 0 < n < 10 and 0 < m < 10 == False:
        print("ERROR")
        exit()
    if n == "" or m == "":
        print("Nuestra script necesita que se introduzcan dos números, el primero que indica el número de filas de nuestra tabla y el segundo el número de columnas.")
        exit()

    for i in range(n):
        print()
        for j in range(m):
            print("*", end='')
```

## Código Main

```
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
```
