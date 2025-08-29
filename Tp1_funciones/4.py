def ingresar_valores() -> int:

    '''
    pide al usuario dos numeros enteros correspondientes al total de la compra y el dinero recibido.

    Pre: no ingresan parametros.

    Post: retornan dos valores enteros
    '''

    total_de_compra = int(input('Ingrese el total de la compra: '))
    dinero_recibido = int(input('Ingrese el dinero recibido: '))
    return total_de_compra, dinero_recibido


def verificar_vuelto(total_de_compra:int, dinero_recibido:int) -> bool:
    '''
    verifica si el dinero recibido es menor que el total de compra, tambien verifica si el dinero recibido es igual al importe, y si el dinero recibido es mayor al importe, si es ahi, ingresa a la funcion que calcula cuando es el veulto.
    
    Pre: ingresa dos numeros enteros, uno corresponde al total de la compra y el segundo al dinero recibido.
    
    Post: si el dinero recibido es menor o igual al precio total, la funcion imprime un mensaje para el usuario. si es mayor ingresa a la funcion calculo_del_vuelto.
    '''
    if dinero_recibido < total_de_compra:
        print('PAGO INSUFICIENTE')
    elif dinero_recibido == total_de_compra:
        print('NO TIENE VUELTO')
    elif dinero_recibido > total_de_compra:
        return True

def calculo_del_vuelto(total_de_compra: int, dinero_recibido: int) -> list[int]:

    '''
    calcula y guarda la cantidad de billetes de cada valor que debe devolver y guarda el valor del billete.
    
    Pre: ingresa dos numeros enteros.
    
    post: devuelve dos listas de enteros.
    '''

    billetes = [5000,1000,500,200,100,50,10]
    resto_a_devolver = dinero_recibido - total_de_compra
    valor_billete = []
    cant_billetes = []


    for i in billetes:
        cant_billetes.append(resto_a_devolver//i)
        valor_billete.append(i)
        resto_a_devolver = resto_a_devolver % i


    if resto_a_devolver == 0:
        for c, b in zip(cant_billetes, valor_billete):
            print(f'{c} billetes de {b}')
    else:
        print('cantidad de dinero en caja insuficiente.')


def main():
    total_de_compra, dinero_recibido = ingresar_valores()
    valor = verificar_vuelto(total_de_compra, dinero_recibido)
    if valor == True:
        calculo_del_vuelto(total_de_compra, dinero_recibido)
        

if __name__ == '__main__':
    main()
