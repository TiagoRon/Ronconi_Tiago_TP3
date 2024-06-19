# quince.py
from canciones import informacion

def insercion_ordenamiento(arr, key, compare):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j][key], key_item[key]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def compare_strings(a, b):
    return a.lower() > b.lower()

def compare_numbers(a, b):
    return a > b

def ordenar_por_nombre(canciones):
    return insercion_ordenamiento(canciones, 'Nombre', compare_strings)

def ordenar_por_artista(canciones):
    return insercion_ordenamiento(canciones, 'Artista', compare_strings)

def ordenar_por_lanzamiento(canciones):
    return insercion_ordenamiento(canciones, 'Lanzamiento', compare_numbers)


def esta_la_banda(canciones):
    audioslave_encontrado = False
    rolling_stones_encontrado = False
    
    for cancion in canciones:
        if cancion["Artista"] == "Audioslave":
            audioslave_encontrado = True
        elif cancion["Artista"] == "The Rolling Stones":
            rolling_stones_encontrado = True
    
    print(f"Audioslave: {'Si esta' if audioslave_encontrado else 'No esta'}")
    print(f"The Rolling Stones: {'Si esta' if rolling_stones_encontrado else 'No esta'}")


def mostrar_nirvana(canciones):
    temas = []
    for cancion in canciones:
        if cancion["Artista"] == "Nirvana":
            temas.append(cancion["Nombre"])
    for tema in temas:
        print(tema)

def canciones_rhcp(canciones):
    temas = 0

    for cancion in canciones:
        if cancion["Artista"] == "Red Hot Chili Peppers":
            temas += 1

    return temas

def info_canciones(canciones):

    artista = None
    lanzamiento = None
    seg_artista = None
    seg_lanzamiento = None


    for cancion in canciones:
        if cancion["Nombre"] == "Fake tales of San Francisco":
            artista = cancion["Artista"]
            lanzamiento = cancion["Lanzamiento"]
        elif cancion["Nombre"] == "Black Hole Sun":
            seg_artista = cancion["Artista"]
            seg_lanzamiento = cancion["Lanzamiento"]
    print(f"Información de Fake Tales of San Francisco:")
    print(f"Artista: {artista}")
    print(f"Lanzamiento: {lanzamiento}")
    print(" ")
    print(f"Información de Black Hole Sun:")
    print(f"Artista: {seg_artista}")
    print(f"Lanzamiento: {seg_lanzamiento}")



print("Ordenado por Nombre:")
for cancion in ordenar_por_nombre(informacion):
    print(cancion)

print("Ordenado por Artista:")
for cancion in ordenar_por_artista(informacion):
    print(cancion)

print("Ordenado por Lanzamiento:")
for cancion in ordenar_por_lanzamiento(informacion):
    print(cancion)

print(" ")

esta_la_banda(informacion)

print(" ")

print("Todos los temas de nirvana:")
mostrar_nirvana(informacion)

print(" ")

numero_temas = canciones_rhcp(informacion)

print(f"Red Hot Chili Peppers tienen {numero_temas} temas")

print(" ")

info_canciones(informacion)
