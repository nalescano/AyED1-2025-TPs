
def gasto_total_mensual(cant_viajes_mensuales: int) -> int:
    
    '''
    multiplica la cantidad de viajes hechos en un mes por la tarifa actual.

    Pre: recibe un numero entero.

    Post: devuelve un entero que es el valor total.
    '''
    
    gasto_total = cant_viajes_mensuales * 1000
    return gasto_total


def calcular_importe_final() -> None:

    '''
    pide al usuario un valor entero correspondiente a la cantidad de viajes que realizo en un mes. Luego llama a una funcion para calcular el valor total del mes y despues aplica el descuento segun la cantidad de viajes realizados.

    Pre: ingresa como parametro un entero.

    Post: no retorna nada, solo imprime un mensaje por consola.
    '''

    cant_viajes_mensuales = int(input('Ingrese la cantidad de viajes realizados en un mes: '))

    gasto_total = gasto_total_mensual(cant_viajes_mensuales)

    if cant_viajes_mensuales <= 20:
        print('el total gastado en el mes es de: ', (gasto_total))

    elif cant_viajes_mensuales <= 30 and  cant_viajes_mensuales >= 21:
        descuento_20 = gasto_total * 20 / 100
        print('el total gastado en el mes es de: ', (gasto_total - descuento_20))

    elif cant_viajes_mensuales <= 40 and cant_viajes_mensuales >= 31:
        descuento_30 = gasto_total * 30 / 100
        print('el total gastado en el mes es de: ', (gasto_total - descuento_30))

    elif cant_viajes_mensuales >= 41:
        descuento_40 = gasto_total * 40 / 100
        print('el total gastado en el mes es de: ', (gasto_total - descuento_40))


def main():
    '''
    funcion principal.
    pre: no recibe ningun parametro.
    post: ejecuta la logica principal del programa. no retorna ningun valor
    '''
    calcular_importe_final()

if __name__ == '__main__':
    main()
