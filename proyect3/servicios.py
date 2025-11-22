def agregar_producto(inventario, nombre, precio, cantidad):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return False
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(nuevo_producto)
    return True

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventarrio vacio")
        return
    print("NOMBRE     PRECIO     CANTIDAD    SUBTOTAL")
    for prod in inventario:
        subtotal = prod["precio"] * prod["cantidad"]
        print(prod["nombre"], prod["precio"], prod["cantidad"], subtotal)

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    prod = buscar_producto(inventario, nombre)
    if prod is None:
        return False
    if nuevo_precio is not None:
        prod["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        prod["cantidad"] = nueva_cantidad
    return True

def eliminar_producto(inventario, nombre):
    prod = buscar_producto(inventario, nombre)
    if prod:
        inventario.remove(prod)
        print("Eliminado")
        return True
    else:
        print("No encontrado")
        return False

def calcular_estadisticas(inventario):
    if not inventario:
        return None
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum((lambda p: p["precio"] * p["cantidad"])(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }
