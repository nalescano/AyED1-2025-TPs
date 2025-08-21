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
    if anio > 0:
        return True
    
def verificar_mes(mes:int) -> bool:
    if mes > 0 or mes < 12:
        return True
    
def verificar_si_es_bisiesto(anio, dias_por_mes) -> str:
    if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0):
        dias_por_mes[2] = 29
        print('Es año bisiesto')


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