def palindromo (palabra: str):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def main ():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    message = 'Es palíndromo' if es_palindromo else 'No es palíndromo'
    print(message)


if __name__ == '__main__':
    main()
