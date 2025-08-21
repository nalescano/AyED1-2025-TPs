import random

def crear_lista():
    cantidad = random.randint(1,5)
    lista_random = [random.randint(1000, 9999) for i in range(cantidad)]
    print("Lista generada: ", lista_random)
    return lista_random

def calcular_producto(lista):
    total_producto = 1
    for nro in lista:
          total_producto = total_producto * nro
    print("Producto de todos los elementos: ", total_producto)
    return total_producto

def eliminar_valor(lista, valor_a_eliminar):
    lista.find(valor_a_eliminar)
    lista.remove(valor_a_eliminar)
    print(lista)

def main():
    lista = crear_lista()
    calcular_producto(lista)
    valor_a_eliminar = int(input("Ingrese el valor a eliminar: "))
    eliminar_valor(lista, valor_a_eliminar)

if __name__ == "__main__":
    main()

