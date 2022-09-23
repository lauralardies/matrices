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