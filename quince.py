from pokemon import entrenadores

def cantidad_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            return len(entrenador["pokemons"])
    return 0 

def entrenadores_3_victorias(entrenadores):
    entrenadores_victorias = []
    for entrenador in entrenadores:
        if entrenador["torneos_ganados"] >= 3:
            entrenadores_victorias.append(entrenador["nombre"])
    return entrenadores_victorias

def pokemon_mayor_nivel_del_mejor_entrenador(entrenadores):
    mejor_entrenador = entrenadores[0]
    for entrenador in entrenadores:
        if entrenador["torneos_ganados"] > mejor_entrenador["torneos_ganados"]:
            mejor_entrenador = entrenador

    pokemon_mayor_nivel = mejor_entrenador["pokemons"][0]
    for pokemon in mejor_entrenador["pokemons"]:
        if pokemon["nivel"] > pokemon_mayor_nivel["nivel"]:
            pokemon_mayor_nivel = pokemon
    
    return pokemon_mayor_nivel

def info_entrenadores(entrenador_nombre):
    for entrenador in entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            print(f"Informacion de {entrenador_nombre}")
            print(f"Torneos Ganados: {entrenador['torneos_ganados']}")
            print(f"Batallas Perdidas: {entrenador['batallas_perdidas']}")
            print(f"Batallas Ganadas: {entrenador['batallas_ganadas']}")
            pokemones = entrenador["pokemons"]
            print("Pokemones:")
            for pokemon in pokemones:
                print(f"- {pokemon['nombre']} (Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}", end="")
                if "subtipo" in pokemon:
                    print(f", Subtipo: {pokemon['subtipo']}", end="")
                print(")")
            break
    else:
        print(f"No se encontro al entrenador con nombre {entrenador_nombre}")

def entrenadores_alto_porcentaje(entrenadores):
    entrenadores_altos = []

    for entrenador in entrenadores:
        total_batallas = entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"]
        porcentaje_ganadas = (entrenador["batallas_ganadas"] / total_batallas) * 100
        if porcentaje_ganadas > 79:
            entrenadores_altos.append(entrenador["nombre"])
    
    if entrenadores_altos:
        print("Entrenadores con mas del 79% de batallas ganadas:")
        for nombre in entrenadores_altos:
            print(nombre)
    else:
        print("No hay entrenadores con mas del 79% de batallas ganadas")
    print("")

def entrenadores_con_pokemons_especificos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        tiene_fuego_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador["pokemons"]:
            if pokemon["tipo"] == "Fuego" and pokemon.get("subtipo") == "Planta":
                tiene_fuego_planta = True
            if pokemon["tipo"] == "Agua" and pokemon.get("subtipo") == "Volador":
                tiene_agua_volador = True
        if tiene_fuego_planta or tiene_agua_volador:
            resultado.append(entrenador["nombre"])
    return resultado

def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            niveles = [pokemon["nivel"] for pokemon in entrenador["pokemons"]]
            return sum(niveles) / len(niveles) if niveles else 0
    return 0

def cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    cantidad = 0
    for entrenador in entrenadores:
        for pokemon in entrenador["pokemons"]:
            if pokemon["nombre"] == nombre_pokemon:
                cantidad += 1
                break
    return cantidad

def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon["nombre"] for pokemon in entrenador["pokemons"]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador["nombre"])
    return resultado

def entrenadores_con_pokemons_especificos_lista(entrenadores):
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    resultado = []
    for entrenador in entrenadores:
        for pokemon in entrenador["pokemons"]:
            if pokemon["nombre"] in pokemons_especificos:
                resultado.append(entrenador["nombre"])
                break
    return resultado

def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador["nombre"] == nombre_entrenador:
            for pokemon in entrenador["pokemons"]:
                if pokemon["nombre"] == nombre_pokemon:
                    print(f"Entrenador: {entrenador['nombre']}")
                    print(f"Pokemon: {pokemon['nombre']}")
                    print(f"Nivel: {pokemon['nivel']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    if "subtipo" in pokemon:
                        print(f"Subtipo: {pokemon['subtipo']}")
                    return True
    return False

pokemon = pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)
entrenadores_con_victorias = entrenadores_3_victorias(entrenadores)
entrenadores_alto_porcentaje(entrenadores)

print("Entrenadores con 3 o mas victorias:")
for nombre in entrenadores_con_victorias:
    print(nombre)

print("")

print(f"El Pokemon de mayor nivel del entrenador con mas torneos ganados es {pokemon['nombre']} de nivel {pokemon['nivel']}.")

print("")

print("Entrenadores con Pokemons de tipo fuego y planta o agua/volador:")
print(entrenadores_con_pokemons_especificos(entrenadores))

print("")

print("Promedio de nivel de los Pokemons de 'Ash Ketchum':")
print(promedio_nivel_pokemons(entrenadores, "Ash Ketchum"))

print("")

print("Cantidad de entrenadores con el Pokemon 'Pikachu':")
print(cantidad_entrenadores_con_pokemon(entrenadores, "Pikachu"))

print("")

print("Entrenadores con Pokemons repetidos:")
print(entrenadores_con_pokemons_repetidos(entrenadores))

print("")

print("Entrenadores con los Pokemons Tyrantrum, Terrakion o Wingull:")
print(entrenadores_con_pokemons_especificos_lista(entrenadores))

print("")

print("¿El entrenador 'Ash Ketchum' tiene el Pokemon 'Pikachu'?:")
print(entrenador_tiene_pokemon(entrenadores, "Ash Ketchum", "Pikachu"))
