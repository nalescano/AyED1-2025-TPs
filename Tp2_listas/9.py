

def multiplos_7(a:int, b:int) -> list:
    '''
    crea una lista con los valores de A y V que sean multiplos de 7 pero no se 5.

    Pre:
        - ingresan 2 numeros enteros (a , b)
    
    Post: 
        - devuelve una lista de enteros con los numeos que cumplan la condicion.
    '''
    
    return [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]


def main() -> None:
    '''
    funcion principal.
    - pide dos numeros enteros positivos al usuario.
    - llama a la funcion que filtra los numeros multiplos de 7 que hay entre los dos numeros ingresados
    
    '''

    a = int(input('ingrese un numero A: '))
    b = int(input('ingrese un numero B: '))

    numeros_multiplos_7 = multiplos_7(a,b)
    print(numeros_multiplos_7)


if __name__ == '__main__':
    main()