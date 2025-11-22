nombre = input("Ingrese el nombre del producto: ")

# Validación del precio con bucle
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            break
        else:
            print("Error: El precio debe ser mayor que cero.")
    except ValueError:
        print("Error: El precio debe ser un número válido.")

# Validación de la cantidad con bucle
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser mayor que cero.")
    except ValueError:
        print("Error: La cantidad debe ser un número entero válido.")

# Cálculo del total
total = precio * cantidad

# Mostrar resumen del producto
print("--- RESUMEN DEL PRODUCTO ---")
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", total)

#Este programa funciona de la siguiente manera, se inserta el nombre del producto que se va a comprar.
# Una vez insertado el nombre del producto, se hace un bucle el cual revisa el precio del producto, en caso de que el precio es menor a 0 este le va a tirar que debe de ser mayor a cero, o si se pone una letra le dice que es cantidad incorrecta
# Se maneja en Decimal
# despues en cantidad es similar al precio pero se usa enteros, ya que no se pide un producto por partes (no pues como si pidieras mitad de ram y te dan un stick partido XDDDD)
# despues de hacer los calculos del precio por la cantidad, te da un resumen de el nombre de tu producto, su precio base y cuantos productos llevas, y te dice el precio final