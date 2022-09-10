def main () -> None:
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    #Reto 1
    contador = 0
    while contador < 10:
        if contador % 2 != 0:
            contador += 1
            continue
        print(contador)
        contador += 1

    #Reto 2
    i = 0
    while i < 100:
        print(i)
        if i == 56:
            break
        i += 1

    #Reto 3
    texto = input('Escribe un texto: ')
    letra = 'a'
    i = 0
    while True:
        letra = texto[i]
        if letra == 'o':
            break
        print(letra)
        i += 1


if __name__ == '__main__':
    main()
