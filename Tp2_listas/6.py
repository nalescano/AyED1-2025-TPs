
def cargar_lista() -> list:
    '''
    arma una lista con la n cantidad de posiciones que ingresan por consola con los nros que ingresan por consola.

    Pre:
        - no ingresa ningun valor como parametro.

    Post:
        - retorna una lista de enteros.
    '''
    lista = []

    cantidad_posiciones = int(input('ingrese un nro para las posiciones: '))

    for i in range(1, cantidad_posiciones +1):
        nro = int(input('ingrese un nro para agregar a la lista: '))
        lista.append(nro)

    return lista


def normalizar(lista_enteros: list) -> list:
    '''
    normaliza los elementos de una lista para que den como resultado 0.1

    Pre:
        - ingresa una lista de enteros como parametro.

    Post: 
        - devuelve una lista con los numeros normalizados.
    '''

    suma_total = sum(lista_enteros)

    return [elem / suma_total for elem in lista_enteros]


def main() -> None:
    '''
    Funcion principal.
    - llama a las funciones para cargar lista y normalizar lista.
    '''

    lista_enteros = cargar_lista()

    lista_normalizada = normalizar(lista_enteros)
    print(f'lista normalizada: {lista_normalizada}')


if __name__ == '__main__':
    main()