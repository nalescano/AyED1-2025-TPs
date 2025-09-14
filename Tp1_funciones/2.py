def validar_anio(anio:int) -> bool:
    '''
    verifica que el anio que ingresa sea menor al anio actual.
    
    pre: 
        - un numero entero positivo (anio).
    post: 
        - devuelve (True) si el anio es menor a 2025.
        - si es mayor muestra un mensaje en consola y retorna (False).
    '''

    if anio <= 2025:
        return True
    else:
        print('el anio que ingreso todavia no ocurrio')
        return False


def verificar_bisiesto(anio: int, mes_2: int) -> bool:
    '''
    verifica si el entero es divisible por 400 y 2.
    
    pre: 
        - dos enteros positivos (anio y mes_2)
    post: 
        - devuelve (True) si el anio es divisible por 400 o por 4.
        - si no es divisible devuelve (False)
    '''

    if (anio % 400 == 0) or (anio % 4 == 0):
        mes_2 = 29
        print('el anio que ingreso es bisiesto')
        return True
    else: return False
    
    
def verifiar_dia(dia: int, mes: int, mes_30: list[int], mes_31: list[int], es_bisiesto: bool) -> bool:
    '''
    verifica que el dia que ingreso sea valido.
    
    Pre: 
        - dos enteros positivos (dia y mes).
        - dos listas de enteros (meses con 30 y con 31 dias).
        - un booleano (indica si el anio es bisiesto).
    post: 
        - devuelve (True) si el dia corresponde a un mes valido y respeta el rango de dias permitidos (considerando febrero y los anios bisiestos).
        - devuelve (False) en caso contrario.
    '''

    if (dia <= 0) or (dia > 31):
        return False
    elif mes in mes_30:
        if dia <= 30:
            return True
        else: 
            return False
    elif mes in mes_31:
        if dia <= 31:
            return True
        else:
            return False
    elif mes == 2:
        if dia <= 28:
            return True
        elif es_bisiesto == True:
            dia = 29
            return True
        else:
            return False
    else: return False


def verificar_fecha(dia: int, mes: int, anio: int) -> None:
    ''' 
    verifica si la fecha ingresada es valida.

    pre: 
        - tres enteros positivos (dia, mes, anio).
    post: 
        - muestra en consola un mensaje.
    '''

    mes_30 = [4, 6, 9, 11]
    mes_31 = [1, 3, 5, 7, 8, 10, 12]
    mes_2 = 28

    anio_es_valido = validar_anio(anio)
    es_bisiesto = verificar_bisiesto(anio, mes_2)
    dia_es_valido = verifiar_dia(dia, mes, mes_30, mes_31, es_bisiesto)

    if anio_es_valido and dia_es_valido == True:
        print('la fecha que ingreso es valida')
    else:
        print('la fecha que ingreso no es valida')


def main() -> None:
    '''
    funcion principal.
    pre:
        - no recibe parametros.

    post: 
        - solicita al usuario tres numeros enteros (dia, mes y anio)
        - llama a la funcion verificar_fecha
    
    '''
    dia = int(input('ingrese un nro del 1 al 30 - 31: '))
    mes = int(input('ingrese un nro del 1 al 12: '))
    anio = int(input('ingrese un nro de 4 digitos: '))

    verificar_fecha(dia, mes, anio)

if __name__ == '__main__':
    main()