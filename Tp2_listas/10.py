import random


def main() -> None:
    '''
    funcion principal.

    - genera una lista de numeros random del 1 al 100 con una cantidad random de posiciones del 10 al 20.
    - crea una nueva lista en donde se agregan los numeros impares de la lista random. 

    '''

    lista_random = [random.randint(1,100) for i in range(random.randint(10,20))]
    print(lista_random)

    lista_de_impares = list(filter(lambda i:i % 2 !=0, lista_random))
    print(lista_de_impares)

if __name__ == '__main__':
    main()