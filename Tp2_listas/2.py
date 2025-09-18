import random

def generar_lista(largo_de_lista: int)-> list[int]:
    '''
    carga una lista con n cantidad de numeros aleatorios de cuatro digitos.

    Pre: ingresa un numero entero para cargar las posiciones.

    Post: devuelve una lista de enteros.
    '''
    lista_numeros = [random.randint(1, 100) for i in range(largo_de_lista)] 
    return lista_numeros


def lista_sin_repetidos(lista_de_numeros:list)-> bool:
    '''
    verifica que hay un elemento repetido en la lista.

    Pre: 
        - ingresa una lista de numeros enteros (lista_de_nuemeros).

    Post: 
        - devuelve una nueva lista de enteros con los numeros unicos de la lista recibida (lista_de_numeros).
    '''

    for i in range(len(lista_de_numeros)):
        unicos = []
        for i in lista_de_numeros:
            if i not in unicos:
                unicos.append(i)
        return unicos


def main()-> None:
    '''
    funcion principal.
    
    pre:
        - no ingresa ningun valor como parametro.
    
    post:
        - llama a las funciones principales.
    '''

    largo_de_lista = int(input('ingrese un nro entero: '))
    lista_de_numeros = generar_lista(largo_de_lista)

    print(lista_de_numeros)

    repetidos = [2, 5, 2, 8, 9, 25]

    sin_repetidos = lista_sin_repetidos(repetidos)
    print(f'nueva lista sin repetidos: {sin_repetidos}')

if __name__ == '__main__':
    main()
