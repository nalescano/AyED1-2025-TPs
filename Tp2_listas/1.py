import random

def crear_lista() -> list[int]:
    '''
    crea una lista con una capacidad random de 1 a 5 posiciones, y agrega enteros random de cuatro cifras. luego imprime la lista. 
    
    Pre: 
        - no ingresa nada como parametro.
    
    Post: 
        - devuelve una lista de enteros.
    '''
    lista_random = [random.randint(1000, 9999) for i in range(random.randint(1,5))]
    return lista_random


def calcular_producto(lista_de_enteros: list) -> int:
    '''
    recorre la lista y multiplica cada valor.

    Pre: 
        - ingresa como parametro una lista de enteros.
    
    Post: 
        - devuelve un entero (total de los numeros multiplicados).
    '''
    total_producto = 1
    for nro in lista_de_enteros:
          total_producto *= nro

    return total_producto


def eliminar_valor(lista_de_enteros:list[int], valor_a_eliminar:int) -> None:
    '''
    busca en la lista el valor que ingresa como parametro y lo elimina.

    Pre: 
        - ingresa una lista de enteros.
        - ingresa un entero (valor_a_eliminar).
    
    Post: 
        - devuelve la lista con el digito eliminado.
    '''

    if valor_a_eliminar in lista_de_enteros:
        lista_de_enteros.remove(valor_a_eliminar)
    return lista_de_enteros



def verificar_capicua(nueva_lista:list) -> bool:
    '''
    crea una lista y verifica si es capicua.
    
    Pre:
        - no ingreda nada como parametro.
    
    Post: 
        - devuelve True si el primer valor coincide con el ultimo y lo mismo con el anteultimmo. y devuelve False si no coinciden
    '''

    if nueva_lista == nueva_lista[::-1]:
        return True
    else:
        return False
            

def main()-> None:
    '''
    funcion principal.

    pre:
        - no ingresa ningun valor como parametro.
    post:
        - llama a las funciones principales.
    '''

    lista_de_enteros = crear_lista()
    print(f'lista generada: {lista_de_enteros}')
    
    producto = calcular_producto(lista_de_enteros)
    print(f'total de la lista calculada: {producto}')
    
    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    nueva_lista = eliminar_valor(lista_de_enteros, valor_a_eliminar)
    print(f'nueva lista sin el valor: {nueva_lista}')
    
    if verificar_capicua(nueva_lista):
        print('es capicua')
    else:
        print('no es capicua')


if __name__ == "__main__":
    main()
