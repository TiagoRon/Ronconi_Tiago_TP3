from personajes import superheroes

def eliminar_linterna_verde():
    global superheroes
    superheroes = [heroe for heroe in superheroes if heroe["nombre"] != "Linterna Verde"]

def wolverine_año():
    for superheroe in superheroes:
        if superheroe["nombre"] == "Wolverine":
            return superheroe["Año de aparicion"]
    return None  

def cambiar_casa_dr_strange():
    for superheroe in superheroes:
        if superheroe["nombre"] == "Dr. Strange":
            superheroe["Casa de comic"] = "Marvel"
            print("Se ha cambiado la casa de Dr Strange a Marvel")
            return

def buscar_traje_o_armadura():
    superheroes_con_traje_armadura = []  # Lista para almacenar nombres de superhéroes con "traje" o "armadura"
    
    for superheroe in superheroes:
        biografia = superheroe["Biografia"]
        if "traje" in biografia.lower() or "armadura" in biografia.lower():
            superheroes_con_traje_armadura.append(superheroe["nombre"])
    return superheroes_con_traje_armadura

def aparicion_1963():
    personajes_aparicion_1963 = []

    for superheroe in superheroes:
        año = superheroe["Año de aparicion"]
        if año >= 1963:
            personajes_aparicion_1963.append(superheroe["nombre"])
    return personajes_aparicion_1963

def capitan_mujer_casa():
    capita_america_casa = None
    mujer_maravilla_casa = None

    for superheroe in superheroes:
        if superheroe["nombre"] == "Captain America":
            capita_america_casa = superheroe["Casa de comic"]
        elif superheroe["nombre"] == "Wonder Woman":
            mujer_maravilla_casa = superheroe["Casa de comic"]
    return capita_america_casa, mujer_maravilla_casa

def mostrar_informacion(superheroe_nombre):
    for superheroe in superheroes:
        if superheroe['nombre'] == superheroe_nombre:
            print(f"Información de {superheroe_nombre}:")
            print(f"Nombre: {superheroe['nombre']}")
            print(f"Año de aparición: {superheroe['Año de aparicion']}")
            print(f"Casa de comic: {superheroe['Casa de comic']}")
            print(f"Biografía: {superheroe['Biografia']}")
            print() 

def superheroes_por_letra(letra):
    superheroes_letra = []

    for superheroe in superheroes:
        if superheroe["nombre"].startswith(letra):
            superheroes_letra.append(superheroe["nombre"])
    return superheroes_letra

def contar_superheroes_por_casa():
    casa_comic_cuenta = {"DC": 0, "Marvel": 0}

    for superheroe in superheroes:
        if superheroe["Casa de comic"] == "DC":
            casa_comic_cuenta["DC"] += 1
        elif superheroe["Casa de comic"] == "Marvel":
            casa_comic_cuenta["Marvel"] += 1
    return casa_comic_cuenta

año = wolverine_año()
superheroes_traje_armadura = buscar_traje_o_armadura()
superheroes_1963 = aparicion_1963()
capitan_casa, mujer_maravilla_casa = capitan_mujer_casa()
superheroes_B = superheroes_por_letra("B")
superheroes_M = superheroes_por_letra("M")
superheroes_S = superheroes_por_letra("S")
conteo_casa_comic = contar_superheroes_por_casa()


eliminar_linterna_verde()


print(" ")
if año is not None:
    print(f"La aparición de Wolverine fue en {año}")
else:
    print("Wolverine no fue encontrado en la lista de superheroes")

print(" ")
if superheroes_traje_armadura:
    print("Superheroes con traje o armadura en su biografia:")
    for nombre in superheroes_traje_armadura:
        print(nombre)
else:
    print("No se encontraron superheroes con traje o armadura en su biografia")

print("")
if superheroes_1963:
    print("Superheroes que debutaron en 1963 o despues:")
    for nombre in superheroes_1963:
        print(nombre)
else:
    print("No se encontraron superheroes que debutaran en 1963 o despues")

print("")

print(f"Casa de Capitan America: {capitan_casa}")
print(f"Casa de Mujer Maravilla: {mujer_maravilla_casa}")

print("")

mostrar_informacion("Flash")
mostrar_informacion("Star-Lord")

print("Superheroes que comienzan con la letra B:")
print(superheroes_B)
print("")

print("Superheroes que comienzan con la letra M:")
print(superheroes_M)
print("")

print("Superheroes que comienzan con la letra S:")
print(superheroes_S)
print("")

print("Numero de superheroes por casa de comic:")
print(f"DC: {conteo_casa_comic['DC']}")
print(f"Marvel: {conteo_casa_comic['Marvel']}")