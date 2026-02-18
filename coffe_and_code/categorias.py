def agregar_categoria(categorias: set, nueva: str)-> None:
    pass

def eliminar_categoria(categorias: set, nombre: str) -> None:
    if nombre not in categorias:
        print(f"La categoria {nombre} no existe en el conjunto.")
        return
    categorias.discard(nombre)
    print(f"Categoría {nombre} eliminada correctamente.")

def unir_categorias(principales: set, temporada: set) -> set:
    catalogo_completo = principales | temporada
    print("\nUnión de categorías (catalogo completo):")
    print("-" * 40)
    for categoria in sorted(catalogo_completo):
        print(f"   -{categoria}")
    print()
    return catalogo_completo

def buscar_categoria(categorias: set, nombre: str) -> bool:
    encontrada = nombre in categorias
    if encontrada:
        print(f"Sí, está en las categorías principales")
    else:
        print(f"{nombre} No está en las categorías principales")


def imprimir_categorias(categorias: set, titulo: str = "Categorias") -> None:
    print(f"\n {titulo}:")
    print("-" * 40)
    for categoria in sorted(categorias):
        print(f" -{categoria}")
    print()
