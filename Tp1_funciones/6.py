
def concatenacion_enteros():
    nro1 = int(input('ingrese el primer nro: '))
    nro2 = int(input('ingrese el segundo nro: '))
    valor_retorno = nro1 * 1000 + nro2
    return valor_retorno

def main():
    valor = concatenacion_enteros()
    print(valor)

if __name__ == '__main__':
    main()