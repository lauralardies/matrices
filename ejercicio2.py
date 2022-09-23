def longitud(str):
	contador = 0
	for i in str:
		contador += 1
	return contador

def condicion(str):
    if longitud(str) >= 3 and longitud(str) < 10:
        return True
    else:
        return False