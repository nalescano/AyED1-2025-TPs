
def verificar_orden(lista_enteros:list) -> bool:
    '''
    verifica si la lista está ordenada.

    Pre:
        - ingresa una lista de enteros (lista_enteros).

    Post:
        - devuelve True si esta ordenado.
        - devuelve False si la lista esta desordenado.
    '''

    esta_ordenado = True

    for i in range(len(lista_enteros) -1):
        if lista_enteros[i] > lista_enteros[i +1]:
            esta_ordenado = False
            break

    return esta_ordenado

def main() -> None:
    '''
    funcion principal.

    pre:
        - no ingresa ningun valor como parametro.

    post:
        - llama a las funciones principales.
    '''

    lista_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    orden = verificar_orden(lista_enteros)
    print(orden)


if __name__ == '__main__':
    main()