numeros = []

def pedir_numeros(numeros: list[int]) -> list[int]:
    """
    Pide tres números enteros del 1 al 9 al usuario y los agrega a la lista recibida.

    Pre: recibe una lista de enteros vacía.

    Post: la lista "numeros" contendrá tres números ingresados por el usuario.
    """

    for i in range(3):
        numero_usuario = int(input("Ingrese un número desde el 1 al 9: "))
        numeros.append(numero_usuario)
    return numeros

def buscar_nro_mayor(numeros: list[int]) -> None:
    """
    Reccorre la lista de entero y determina el número mayor, siempre que sea único.

    Pre: recibe una lista de enteros cargada por el usuario.

    Post:
        - si algún número aparece más de una vez, se imprime -1.
        - si todos los números son distintos, se imprime el mayor.
    """
    
    for i in numeros:
        if numeros.count(i) > 1:
            print(-1)
            return
    nro_mayor = max(numeros)
    print("El numero mayor es: ", nro_mayor)


def main():
    pedir_numeros(numeros)
    buscar_nro_mayor(numeros)

if __name__ == "__main__":
    main()