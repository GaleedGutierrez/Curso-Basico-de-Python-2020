import random


def main () -> None:
    NUMERO_ALEATORIO = random.randint(1, 100)
    numero_elegido = int(input('Ingresa un número del 1 al 100: '))

    while numero_elegido != NUMERO_ALEATORIO:
        if numero_elegido < NUMERO_ALEATORIO:
            print('Busca en número más grande.')
        else:
            print('Busca en número más pequeño.')
        numero_elegido = int(input('Elige otro número: '))

    print('¡Ganaste!')


if __name__ == '__main__':
    main()
