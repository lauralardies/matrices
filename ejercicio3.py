def lista_recursiva (inicio, fin, n_saltos, l_saltos):
    l = list(range(inicio, n_saltos*l_saltos, l_saltos))
    if l[-1] >= fin:
        if l[-1] > fin:
            l.pop(-1)
        return l
    else:
        l = lista_recursiva(inicio, fin, n_saltos+1, l_saltos)
    return l
