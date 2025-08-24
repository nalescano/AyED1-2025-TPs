def pedir_nros()-> list[int]:
    '''
    pide tres nros enteros, los carga en una lista y los retorna
    Pre: no ingresa ningun parametro a la funcion.
    Post: devuelve tres numeros enteros
    '''
    nros = []
    for i in range(3):
        nro = int(input("ingrese un numero entero: "))
        nros.append(nro)
    return nros


def verificar_si_hay_repetidos(nros:list[int]) -> bool:
    '''
    verifica si en la lista que ingresa hay nros enteros repetidos
    Pre: ingresa una lista de nros enteros
    Post: Devuelve True si los tres nros son distintos, sino devuelve False
    '''
    
    if nros[0] != nros[2]:
        if nros[0] != nros[1]: 
            if nros[1] != nros[2]:
                    return False
            else:
                return True
        else:
            return True
    else:
        return True
    

def devolver_el_mayor(nros:list[int]) -> int:
    '''
    si la funcion verificar_si_hay_repetidos es True compara la lista de nros para buscar el valor mayor
    Pre: ingresa una lista de numeros enteros
    Post: devuelve -1 si hay repetidos en la lista ó, el nro mayor de la lista de enteros.
    '''

    if verificar_si_hay_repetidos(nros) == True:
        return -1
    
    else:
        nro_mayor = 0
        for i in nros:
            if i > nro_mayor:
                nro_mayor = i
        return nro_mayor
        

def main():
    nros = pedir_nros()
    valor = devolver_el_mayor(nros)
    print(valor)


if __name__ == "__main__":
    main()