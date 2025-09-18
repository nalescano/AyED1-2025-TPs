from tabulate import tabulate

def pedir_fecha() -> int:
    '''
    pide al usuario que ingrese una fecha.
    
    Pre:
        - no ingresa nada por parametro.
        
    Post: devuelve una tupla con los tresd enteros ingresados'''

    dia = int(input('ingrese un nro del 1 al 30-31: '))
    mes = int(input('ingrese un nro del 1-12: '))
    anio = int(input('ingrese un nro de 4 digitos: '))

    return dia, mes, anio


def diadelasemana(dia: int, mes: int, año: int) -> int:
    '''
    calcula el dia de la semana de una fecha.

    Pre:
        - ingresan tres enteros (dia, mes, anio).
    Post:
        - devuelve un entero que correspoonde a un dia de la semana.
        0 dom; 1 lun; 2 mar; 3 mie; 4 jue; 5 vie; 6 sab
    '''
    if mes < 3:
        mes = mes + 10
        año = año - 1
    
    else:
        mes = mes - 2
        siglo = año // 100
        año2 = año % 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    
    if diasem < 0:
        diasem = diasem + 7
        
    return diasem

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

def diasdelmes(mes:int, anio:int) -> int:
    '''
    calcular la cantidad de dias que hay en un mes ingresado.
    
    Pre:
        - ingresan dos enteros (mes y anio).

    Post: 
        - devuelve un entero que corresponde a la cantidad de dias del mes.
    
    '''

    es_bisiesto = verificar_bisiesto(anio)

    if mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if es_bisiesto:
            return 29
        else:
            return 28
    else:
        return 31



def nombres_del_mes(mes: int) -> str:
    '''
    devuelve el nombre del mes correspondiente al numero del mes ingresado.

    Pre: 
        - ingresa un entero (mes).

    Post:
        - devulve el nombre del mes.
    '''

    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    if mes in meses.keys():
        return meses[mes]

def imprimir_calendario(mes, anio, nombre_mes):
    

    dia_uno = diadelasemana(1, mes, anio)
    dias_mes = diasdelmes(mes, anio)

    dias_semana = ('D', 'L', 'M', 'M', 'J', 'V', 'S')

    calendario = []
    semana = [''] * dia_uno

    for dia in range(1, dias_mes +1):
        semana.append(dia)
        if len(semana) == 7:
            calendario.append(semana)
            semana = []
    
    if semana: 
        calendario.append(semana)

    print(f'Calendario {nombre_mes} {anio}')
    print(tabulate(calendario, headers=dias_semana, tablefmt='Keys', stralign='right'))

def main():
    
    dia, mes, anio= pedir_fecha()
    nombre_mes = nombres_del_mes(mes)
    imprimir_calendario(mes, anio, nombre_mes)


if __name__ == '__main__':
    main()