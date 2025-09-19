
def lista_cuadrados(n: int) -> list:
    '''
    crea una lista vacia y recorre desde 1 al  n (entero que ingresa el usuario) y agrega a una nueva lista el primer numero al cuadrado.

    Pre:
        - ingresa un entero (n)

    Post:   
        - devuelve una lista con los numeros al cuadrado (cuadrados).
    '''

    cuadrados = []
    for i in range(1, n+1):
        cuadrados.append(i * 2)
    return cuadrados

def main() -> None:
    '''
    funcion principal.

    pre:
        - no ingresa ningun valor como parametro.
    post:
        - llama a las funciones principales.
    '''
    n = int(input('ingrese un numero: '))
    resultados = lista_cuadrados(n)
    
    print(f'últimos 10 valores: ', resultados[-10:])

if __name__ == '__main__':
    main()