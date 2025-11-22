# Estructura: {nombre: {"precio": float, "cantidad": int}}
productos = {}


def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    
    Solicita al usuario el nombre, precio y cantidad del producto.
    Valida que el precio y cantidad sean mayores a 0.
    Verifica que el producto no exista previamente.
    """
    nombre = input("Ingresa el nombre del producto: ")
    
    # Verificar si el producto ya existe
    if nombre in productos:
        print("Error: Este producto ya existe en el inventario.")
    else:
        try:
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto: "))
            
            # Validación: precio y cantidad deben ser positivos
            if precio > 0 and cantidad > 0:
                productos[nombre] = {"precio": precio, "cantidad": cantidad}
                print(f"✓ Producto '{nombre}' agregado correctamente.")
            else:
                print("Error: El precio y la cantidad deben ser mayores a 0.")
        except ValueError:
            print("Error: Debes ingresar números válidos.")


def mostrar_inventario():
    """
    Muestra todos los productos del inventario.
    
    Itera sobre el diccionario de productos y muestra nombre, precio y cantidad.
    Si el inventario está vacío, muestra un mensaje informativo.
    """
    if productos:
        print("--- INVENTARIO ACTUAL ---")
        for nombre, datos in productos.items():
            print(f"Producto: {nombre}")
            print(f"  Precio: ${datos['precio']:.2f}")
            print(f"  Cantidad: {datos['cantidad']} unidades")
            print("-" * 30)
    else:
        print("El inventario está vacío.")


def calcular_estadisticas():
    """
    Calcula y muestra estadísticas del inventario.
    
    Calcula:
    - Total de productos diferentes
    - Valor total del inventario (suma de precio * cantidad)
    - Producto más caro
    - Producto con mayor stock
    """
    if productos:
        print("--- ESTADÍSTICAS DEL INVENTARIO ---")
        
        # Total de productos diferentes
        total_productos = len(productos)
        print(f"Total de productos diferentes: {total_productos}")
        
        # Valor total del inventario
        valor_total = sum(datos["precio"] * datos["cantidad"] for datos in productos.values())
        print(f"Valor total del inventario: ${valor_total:.2f}")
        
        # Producto más caro
        producto_mas_caro = max(productos.items(), key=lambda x: x[1]["precio"])
        print(f"Producto más caro: {producto_mas_caro[0]} (${producto_mas_caro[1]['precio']:.2f})")
        
        # Producto con mayor stock
        producto_mayor_stock = max(productos.items(), key=lambda x: x[1]["cantidad"])
        print(f"Mayor stock: {producto_mayor_stock[0]} ({producto_mayor_stock[1]['cantidad']} unidades)")
        
    else:
        print("No hay productos para calcular estadísticas.")


def eliminar_producto():
    """
    Elimina un producto del inventario.
    
    Solicita el nombre del producto a eliminar.
    Verifica que el producto exista antes de eliminarlo.
    """
    producto = input("Ingresa el nombre del producto que deseas eliminar: ")
    
    if producto in productos:
        del productos[producto]
        print(f"✓ Producto '{producto}' eliminado correctamente.")
    else:
        print("Error: Producto no encontrado en el inventario.")


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("" + "="*40)
    print("     TIENDA ACHEL - SISTEMA DE INVENTARIO")
    print("="*40)
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadísticas")
    print("4. Eliminar Producto")
    print("5. Salir")
    print("="*40)


# --- PROGRAMA PRINCIPAL ---
# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Ingresa tu opción: ")
    
    # Menú de opciones con validación
    if opcion == "1":
        agregar_producto()
    
    elif opcion == "2":
        mostrar_inventario()
    
    elif opcion == "3":
        calcular_estadisticas()
    
    elif opcion == "4":
        eliminar_producto()
    
    elif opcion == "5":
        print("¡Hasta luego! Gracias por usar el sistema.")
        break  # Salir del bucle y terminar el programa
    
    else:
        print("Error: Opción incorrecta. Por favor elige una opción del 1 al 5.")