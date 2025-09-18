mes_30 = [4, 6, 9, 11]
mes_31 = [1, 3, 5, 7, 8, 10, 12]
mes_2 = 28

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
    
    
def verificar_dia(dia: int, mes: int, mes_30: list[int], mes_31: list[int], es_bisiesto: bool) -> bool:
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

    anio_es_valido = validar_anio(anio)
    
    if anio_es_valido:
        es_bisiesto = verificar_bisiesto(anio, mes_2)
        dia_es_valido = verificar_dia(dia, mes, mes_30, mes_31, es_bisiesto)
    else: print('el anio que ingreso no es valido')

    if anio_es_valido and dia_es_valido == True:
        print('la fecha que ingreso es valida')
        return True
    else:
        print('la fecha que ingreso no es valida')
        return False
    

def dia_siguiente(dia, mes, anio):
    
    #if es_valido:
    if mes in mes_31 == 12 and dia == 31:
        anio +=1

    if mes in mes_30:
        if dia == 30:
            dia = 1
            mes += 1
        else:
            dia +=1

    elif mes in mes_31:
        if dia == 31:
            dia = 1
            mes += 1
        else: dia += 1

    elif mes == 2:
        if dia == 28:
            if  verificar_bisiesto:
                dia = 29
            else: 
                dia = 1
                mes += 1
        else: dia += 1

    print(f' manana es: {dia}/{mes}/{anio}')
    return list(dia, mes, anio)
    

def sumar_dias(dia, mes, anio, es_valido ):
    
    if es_valido:
        n = int(input('ingrese la cantidad de dias que quiere sumar: '))
        i = 0
        while i <= (n-1):
            if dia == 31:
                dia = 1
                mes += 1
            else: dia += 1
            if mes == 12:
                mes = 1
                anio += 1
            i += 1
        print(f'en {n} dias va a ser: {dia}/{mes}/{anio}')
        return list(dia, mes, anio)


def cantidad_dias_existentes():

    fecha_desde = [int(input(f'ingrese {x}: ')) for x in ['dia', 'mes', 'anio']]
    fecha_hasta = [int(input(f'ingrese {x}: ')) for x in ['dia', 'mes', 'anio']]
    cantidad_dias = 0

    if fecha_hasta > fecha_desde:
        while fecha_hasta != fecha_desde:
            fecha_desde = list(dia_siguiente(*fecha_desde))
            cantidad_dias += 1

    print(f'quedan {cantidad_dias} dias para llegar al {fecha_hasta}')


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

    es_valido = verificar_fecha(dia, mes, anio)

    #dia_siguiente(dia, mes, anio, es_valido)

    #sumar_dias(dia, mes, anio, es_valido)

    cantidad_dias_existentes()

if __name__ == '__main__':
    main()
