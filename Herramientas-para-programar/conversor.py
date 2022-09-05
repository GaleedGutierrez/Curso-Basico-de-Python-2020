# Tipo de cambio
ars_usd = 285
cop_usd = 4521.73
mxn_usd = 19.96

menu = """
*** Bienvenido al conversor de monedas 💵💴💶💷 ***

1) Pesos colombianos (COP)
2) Pesos argentinos (ARS)
3) Pesos mexicanos (MXN)

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    moneda = 'COP'
    pesos = float(input(f'¿Cúantos {moneda} tienes?: '))
    dollars = pesos / cop_usd
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print(f'Tienes {dollars}U$D')
elif opcion == '2':
    moneda = 'ARS'
    pesos = float(input(f'¿Cúantos {moneda} tienes?: '))
    dollars = pesos / ars_usd
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print(f'Tienes {dollars}U$D')
elif opcion == '3':
    moneda = 'MXN'
    pesos = float(input(f'¿Cúantos {moneda} tienes?: '))
    dollars = pesos / mxn_usd
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print(f'Tienes {dollars}U$D')
else:
    print('Ingresa una opción correcta, por favor.')
