def crear_inventario(productos: list, datos: dict) -> dict:
    inventario = {}

    for producto in productos:
        inventario[producto] = datos.get(producto, (0, 0.0, 0))

    return inventario

def consultar_producto(inventario: dict, nombre:str)->None:
    if nombre not in inventario:
        print(f"{nombre} no existe en el inventario")
        return
    
    print(f"\n Información de {nombre}: ")
    print(f" - Cantidad en stock: {cantidad} unidades ")
    print(f" - Precio unitario {precio:.2f} $ ")
    print(f" - Nivel de reorden {reorden} unidades ")
    print()

    def imprimir_inventario(inventario: dict) -> None:
        print("\n Inventario completo:")
        print("-" *60)
        print(f"{'Producto':<15} {'Stock':>6}" {'´Precio':>8} {'Reorden':>8})
        print("-" *60)       