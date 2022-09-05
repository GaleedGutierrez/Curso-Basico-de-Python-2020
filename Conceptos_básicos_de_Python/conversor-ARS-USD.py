pesos = input('¿Cúantos pesos argentinos tienes?: ')
pesos = float(pesos)
dolar_value = 285
dollars = pesos / dolar_value
dollars = round(dollars, 2)
dollars = str(dollars)
print(f'Tienes {dollars}U$D')
