def main ():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 45_808_747,
        'Brasil': 213_993_441,
        'Colombia': 51_600_000,
    }

    # print(poblacion_paises['Bolivia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes.')

if __name__ == '__main__':
    main()
