


def lista_cuadrados(n):
    cuadrados = []
    for i in range(1, n+1):
        cuadrados.append(i * 2)
    return cuadrados

def main():
    n = int(input('ingrese un numero: '))
    resultados = lista_cuadrados(n)
    
    print(f'últimos 10 valores: ', resultados[-10:])

if __name__ == '__main__':
    main()