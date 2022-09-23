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