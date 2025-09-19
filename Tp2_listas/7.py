
def intercalar_listas(lista1:list ,lista2: list) -> list:
    '''
    agrega a la lista1 los elementos de la lista2 intercalado.

    Pre:
        - ingresan dos listas de enteros (lista1, lista2)
    
    Post:
        - devuevle la lista1 modificada con los elementos de la lista2.
    '''

    for i in range(len(lista2)):
        lista1.insert(2 * i + 1, lista2[i])
    return lista1


def main() -> None:
    '''
    funcion principal.
    
    pre:
        - no ingresa ningun valor como parametro.
    
    post:
        - llama a las funciones principales.
    '''

    lista1 = [8,1,3]
    lista2 = [5,9,7,]

    lista_intercalada = intercalar_listas(lista1, lista2)
    print(lista_intercalada)

if __name__ == '__main__':
    main()