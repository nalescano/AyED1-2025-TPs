def eliminar_valor(lista_enteros: list, a_eliminar: list) -> list:
    '''
    recorre una lista (a_eliminar) y si el mismo valor esta en la lista (lista_enteros) lo elimina.

    Pre: 
        - ingresan dos lista de enteros (lista_enteros, a_eliminar).

    Post: 
        - devuelve (lista_enteros) con los valores eliminados.
    '''
    for x in a_eliminar:
        while x in lista_enteros:
            lista_enteros.remove(x)
    
    return lista_enteros

def main() -> None:
    '''
    funcion principal.
    
    pre:
        - no ingresa ningun valor como parametro.

    post:
        - llama a las funciones principales.
    '''
    lista_enteros = [1,2,3,4,5,6,7,8,9,10]
    a_eliminar = [2,4,6,8]

    lista_modificada = eliminar_valor(lista_enteros, a_eliminar)
    print(lista_modificada)

if __name__ == '__main__':
    main()