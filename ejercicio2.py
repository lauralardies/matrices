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