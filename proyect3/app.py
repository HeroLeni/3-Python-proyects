import servicios
import archivos

def validar_numero_positivo(mensage, tipo=float):
    while True:
        try:
            valor = tipo(input(mensage))
            if valor < 0:
                print("El valor no puede ser negativo. Intenta de nuveo.")
                continue
            return valor
        except ValueError:
            print("Dato invalido. Escribe un numero valido.")

def opcion_agregar(inventario):
    print("===================")
    print(" AGREGAR NUEVO PROUDUCTO")
    print("===================")
    nombre = input("Nombre del pruducto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    precio = validar_numero_positivo("Precio: $", float)
    cantidad = validar_numero_positivo("Cantidad: ", int)
    if servicios.agregar_producto(inventario, nombre, precio, cantidad):
        print("Producto", nombre, "agregado correctamente")
    else:
        print("Ya existe ese pruducto.")

def opcion_cargar_csv(inventario):
    print("===================")
    print(" CARGAR INVENTARIO DESDE CSV")
    print("===================")
    ruta = input("Ruta del archivo CSV: ").strip()
    if not ruta:
        print("Debes poner ruta de archivo.")
        return
    productos_cargados, filas_invalidas = archivos.cargar_csv(ruta)
    if not productos_cargados and filas_invalidas == 0:
        return
    if not productos_cargados:
        print("Ningun pruducto valido fue cargado.")
        return
    if inventario:
        print("Hay productos previos.")
        opcmenu = input("Desea agragar a la base los productos cargados? SI/NO: ").strip().upper()
        match opcmenu:
            case "SI":
                inventario.extend(productos_cargados)
                print("Productos agregados")
            case "NO":
                print("No se agregaron los productos")
            case _:
                print("Opccion incorecta, no se hace nada")
    else:
        inventario.extend(productos_cargados)
        print("Productos agregados correctamente")
    if filas_invalidas > 0:
        print("Filas invalidas omitidas:", filas_invalidas)

def mostrar_menu():
    print("===============================")
    print("Inventario lada")
    print("===============================")
    print("1. Agregar pruducto")
    print("2. Mostrar inventario")
    print("3. Buscar pruducto")
    print("4. Actualisar pruducto")
    print("5. Eliminar pruducto")
    print("6. Ver estadisitcas")
    print("7. Guardar en CSV")
    print("8. Cargar desde CSV")
    print("9. Salir")
    print("===============================")

def main():
    inventario = []
    print("Bienvenido al inventario lada")
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opcion (1-9): ").strip()
            match opcion:
                case "1":
                    opcion_agregar(inventario)
                case "2":
                    servicios.mostrar_inventario(inventario)
                case "3":
                    nombre = input("Ingrese el nombre a buscar: ")
                    producto = servicios.buscar_producto(inventario, nombre)
                    print(producto if producto else "No se encontro el pruducto.")
                case "4":
                    nombre = input("Nombre a actualizar: ")
                    nuevo_precio = validar_numero_positivo("Nuevo precio: ", float)
                    nueva_cantidad = validar_numero_positivo("Nueva cantidad: ", int)
                    servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                case "5":
                    nombre = input("Pruducto a eliminar: ")
                    servicios.eliminar_producto(inventario, nombre)
                case "6":
                    print(servicios.calcular_estadisticas(inventario))
                case "7":
                    ruta = input("Ruta para guardar CSV: ")
                    archivos.guardar_csv(inventario, ruta)
                case "8":
                    opcion_cargar_csv(inventario)
                case "9":
                    print("Gracias por usar el sistma.")
                    break
                case _:
                    print("Opcion no valida.")
        except Exception as e:
            print("Ocurrio un error fatal:", e)

if __name__ == "__main__":
    main()
