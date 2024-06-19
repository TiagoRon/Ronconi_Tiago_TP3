import random
import time

def generar_lista(tamaño):
    return [random.randint(0, 1000000) for _ in range(tamaño)]

def medir_tiempo(funcion_busqueda, lista, elemento_a_buscar):
    inicio = time.time()
    resultado = funcion_busqueda(lista, elemento_a_buscar)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
    return resultado

def busqueda_lineal(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

lista_100k = generar_lista(100000)
lista_1m = generar_lista(1000000)
lista_10m = generar_lista(10000000)

print("Búsqueda en lista de 100k elementos:")
medir_tiempo(busqueda_lineal, lista_100k, -1)  

print("Búsqueda en lista de 1m elementos:")
medir_tiempo(busqueda_lineal, lista_1m, -1)  

print("Búsqueda en lista de 10m elementos:")
medir_tiempo(busqueda_lineal, lista_10m, -1)  
