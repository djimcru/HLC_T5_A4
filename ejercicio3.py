 def potencia(base, exponete):
    if exponete == 0:
        return 1
    if base == 1:
        return base
    else:
        return base * potencia(base, exponete-1)

print(potencia(2, 3))

    