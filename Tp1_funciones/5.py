
def main():
    un_numero = int(input('ingrese un nro: '))
    es_oblongo = lambda n : any(v * (v+1) == n for v in range(1, n))
    print(es_oblongo(un_numero))

    otro_numero = int(input('ingrese otro numero: '))
    es_triangular = lambda n: any(v*(v+1)/2 == n for v in range(1, n))
    print(es_triangular(otro_numero))

if __name__ == '__main__':
    main()