dollars = input('¿Cúantos dolares tienes?: ')
dollars = float(dollars)
dolar_value = 285
pesos = dolar_value * dollars
pesos = round(pesos, 2)
pesos = str(pesos)
print(f'Tienes ${pesos}')
