# Functiones
def conversor(tipo_pesos: str, valor_dolar: float):
    moneda = tipo_pesos
    pesos = float(input(f'¿Cúantos {moneda} tienes?: $'))
    dollars = pesos / valor_dolar
    dollars = round(dollars, 2)
    print(f'Tienes {dollars}U$D')

# Tipo de cambio
ars_usd = 272
cop_usd = 4480.67
mxn_usd = 20.13

menu = """
*** Bienvenido al conversor de monedas 💵💴💶💷 ***

1) Pesos colombianos (COP)
2) Pesos argentinos (ARS)
3) Pesos mexicanos (MXN)

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor('COP', ars_usd)
elif opcion == '2':
    conversor('ARS', ars_usd)
elif opcion == '3':
    conversor('MXN', ars_usd)
else:
    print('Ingresa una opción correcta, por favor.')
