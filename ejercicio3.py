def potencia(base, exponente):
    if exponente == 0:
        return 1
    if base == 1:
        return base
    else:
        return base * potencia(base, exponente-1)

print(potencia(2, 3))