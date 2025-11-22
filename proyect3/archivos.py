import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("Inventarrio vacio. Nada que guardar.")
        return False
    try:
        directorio = os.path.dirname(ruta)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'precio', 'cantidad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            if incluir_header:
                escritor.writeheader()
            for producto in inventario:
                escritor.writerow(producto)
        print("Inventario guardado en", ruta)
        return True
    except Exception as e:
        print("Error guardando archivo:", e)
        return False

def cargar_csv(ruta):
    productos_cargados = []
    filas_invalidas = 0
    try:
        if not os.path.exists(ruta):
            print("Archivo no exisste.")
            return [], 0
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            if encabezado != ['nombre', 'precio', 'cantidad']:
                print("Encabezado incorrecto")
                if len(encabezado) != 3:
                    return [], 0
            for fila in lector:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0 or not nombre:
                        filas_invalidas += 1
                        continue
                    productos_cargados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except:
                    filas_invalidas += 1
                    continue
        return productos_cargados, filas_invalidas
    except:
        print("Error leyendo archivo")
        return [], 0

def fusionar_inventarios(inventario_actual, productos_nuevos):
    productos_fusionados = 0
    for prd_nuevo in productos_nuevos:
        encontrado = False
        for prd_actual in inventario_actual:
            if prd_actual["nombre"].lower() == prd_nuevo["nombre"].lower():
                prd_actual["precio"] = prd_nuevo["precio"]
                prd_actual["cantidad"] += prd_nuevo["cantidad"]
                productos_fusionados += 1
                encontrado = True
                break
        if not encontrado:
            inventario_actual.append(prd_nuevo)
            productos_fusionados += 1
    return productos_fusionados
