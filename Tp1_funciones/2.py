def recibir_numeros() -> int:
    """
    Pide tres números enteros
    Pre: No recibe parametros iniciales
    Post: Devuelve tres variables enteras
    """

    dia = int(input("Ingrese un día del 1 al 30: "))
    mes = int(input("Ingrese un mes del 1 al 12: "))
    anio = int(input("Ingrese un año (mayor a 0): "))
    return dia, mes, anio

def verificar_anio(anio: int) ->bool:
    '''
    verifica si el anio que se ingreso no sea menor a cero.
    Pre: ingresa el anio que ingreso el usuario.
    Post: devuelve True si el anio es mayor a cero, y False si es menor o igual a cero.
    '''
    if anio >= 0:
        return True
    else:
        return False
    
def verificar_mes(mes:int) -> bool:
    '''
    verifica si el mes que ingreso el usuario es mayor a cero y menor a 12.
    Pre: ingresa el mes que ingreso el usuario.
    Post: devuelve True se el mes es mayor a cero y menor a 12, y False si es mayor a doce o menor a cero.
    '''
    if mes > 0 or mes < 12:
        return True
    else:
        return False
    
def verificar_si_es_bisiesto(anio, dias_por_mes) -> str:
    '''
    verifica si el anio que ingreso el usuario dividido por cuatro, por cien y por cuatrocientos da un resto de cero.
    Pre: ingresa el anio que ingreso el usuario y el diccionario de dias por mes.
    Post: imprime por consola si el anio es bisiesto o no.
    '''
    if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0):
        dias_por_mes[2] = 29
        print('Es año bisiesto')
    else:
        print('el anio no es bisiesto')


def verificar_fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    verifica si el año y el mes es correcto, se crea un diccionario de dias. Y, verifica si el año que se ingreso es bisiesto o no.
    Pre: Recibe tres parametros correspondientes al dia, mes y anio (en ese orden).
    Post: Si los datos ingresados son correctos devuelve True, sino devuelve False
    """

    dias_por_mes = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    verificar_anio(anio)
    
    verificar_mes(mes)

    verificar_si_es_bisiesto(anio, dias_por_mes)
    
    if (verificar_anio == True) and (verificar_mes == True):
        return True
    else:
        return False
    
def mensaje(verificacion:bool) -> str:
    '''
    compara la variable verificacion e imprime un mensaje por consola.
    Pre: Recibe como parametro un booleano de la funcion verificar_fecha_valida
    Post: imprime un mensaje por consola.
    '''
    if verificacion == True:
        print('La fecha que ingreso es correcta')
    else:
        print('La fecha que ingreso es incorrecta')

def main():
    dia, mes, anio = recibir_numeros()
    verificacion = verificar_fecha_valida(dia, mes, anio)
    mensaje(verificacion)

if __name__ == "__main__":
    main()