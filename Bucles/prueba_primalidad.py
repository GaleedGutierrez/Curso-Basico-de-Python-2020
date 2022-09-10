from math import factorial

# def es_primo (numero: int) -> bool:
#     if numero == 1:
#         return True
#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             return False
#     return True



def es_primo (numero: int) -> bool:
    WILSONS_THEOREM = factorial((numero - 1)) + 1
    PRIMO = WILSONS_THEOREM % numero == 0
    return PRIMO


def main () -> None:
    NUMERO = int(input('Escribe un número: '))
    if es_primo(NUMERO):
        print('Es primo.')
    else:
        print('No es primo.')


if __name__ == '__main__':
    main()
