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


def verificar_bisiesto(anio: int) -> bool:
    '''
    verifica si el entero es divisible por 400 y 2.
    
    pre: 
        - dos enteros positivos (anio)
    post: 
        - devuelve (True) si el anio es divisible por 400 o por 4.
        - si no es divisible devuelve (False)
    '''

    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        return True
    else: return False
    
    
def verificar_dia(dia: int, mes: int, es_bisiesto: bool) -> bool:
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
        elif dia == 29:
            if es_bisiesto == True:
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
        es_bisiesto = verificar_bisiesto(anio)
        if es_bisiesto:
            print('el anio que ingreso es bisiesto')
        dia_es_valido = verificar_dia(dia, mes, es_bisiesto)
        if dia_es_valido:
            print('la fecha que ingreso es valida')
            return True

    else: 
        print('la fecha que ingreso no es valida')
        return False
    

def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    '''
    compara los valores (dia, mes y anio) para determinar si los mismos se incrementan, o retornan igual.

    pre: 
        - ingresan tres enteros (dia, mes, anio).
    post:
        - devuelve una tupla con tres enteros (dia, mes, anio).
    '''
    
    if mes == 12 and dia == 31:
        return (1, 1, anio + 1)
    
    elif mes in mes_30:
        if dia == 30:
            return (1, mes +1, anio)
        else:
            return (dia +1, mes, anio)

    elif mes in mes_31:
        if dia == 31:
            return (1, mes +1, anio)
        else: return (dia +1, mes, anio)

    elif mes == 2:
        if (verificar_bisiesto(anio) == True):
            if dia < 29:
                return (dia + 1, mes, anio)
            else:
                return (1, mes +1, anio)
        else:
            if (dia < 28): 
                return (dia +1, mes, anio)
            else:
                return (1, mes +1, anio)


def sumar_dias(dia:int, mes:int, anio:int) -> None:
    '''
    pide un valor entero para contar los dias que tiene que sumar.

    pre:
        - ingresan tres enteros positivos (dia, mes, anio).
    post:
        - devuelve un mensaje por consola.
    '''
    fecha = [dia,mes,anio]
    n = int(input('ingrese la cantidad de dias que quiere sumar: '))
    i = 0
    while i != n:
        fecha = dia_siguiente(*fecha)
        i += 1

    print(f'en {n} dias va a ser: {fecha[0]}/{fecha[1]}/{fecha[2]}')


def cantidad_dias_entre(fecha_desde:tuple, fecha_hasta: tuple) -> int:
    '''
    cuenta cuantos dias hay entre dos fechas.

    Pre:
        - ingresan dos tuplas (fecha_desde, fecha_hasta).
    Post: 
        - devuelve un entero (cantidad_dias).
    '''
    cantidad_dias = 0

    if (fecha_desde[2], fecha_desde[1], fecha_desde[0]) > (fecha_hasta[2], fecha_hasta[1], fecha_hasta[0]):
        fecha1 = fecha_hasta
        fecha2 = fecha_desde
    else: 
        fecha1 = fecha_desde
        fecha2 = fecha_hasta

    while fecha1 != fecha2:
        fecha1 = dia_siguiente(*fecha1)
        cantidad_dias += 1

    return cantidad_dias

def pedir_fecha() -> tuple:
    '''
    pide tres valores enteros al usuario.
    
    Pre:
        - no recibe parametros.
    Post: 
        - devuelve una tupla con tres valores (dia, mes, anio).
    '''
    dia = int(input('ingrese un nro del 1 al 30 - 31: '))
    mes = int(input('ingrese un nro del 1 al 12: '))
    anio = int(input('ingrese un nro de 4 digitos: '))

    return dia, mes, anio

def main() -> None:
    '''
    funcion principal.
    pre:
        - no recibe parametros.

    post: 
        - llama a las funciones principales.
    
    '''
    fecha_a_verificar = pedir_fecha()
    es_valido = verificar_fecha(*fecha_a_verificar)

    if es_valido:
        nuevo_dia, nuevo_mes, nuevo_anio = dia_siguiente(*fecha_a_verificar)
        print(f' manana va a ser: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}')
    
        
    sumar_dias(*fecha_a_verificar)
        

    fecha_desde = pedir_fecha()
    fecha_hasta = pedir_fecha()
    dias = cantidad_dias_entre(fecha_desde, fecha_hasta)
    print(f'quedan {dias} dias hasta {fecha_hasta[0]}/{fecha_hasta[1]}/{fecha_hasta[2]}')


if __name__ == '__main__':
    main()
