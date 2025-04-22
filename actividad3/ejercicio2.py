#Control de inventario de un producto
inventario_inicial = int(input("Ingrese la cantidad incial de inventario: "))
producto_recibido = int(input("Ingrese la cantidad de producto recibido: "))
producto_vendido = int(input("Ingrese la cantidad de producto vendido: "))
suma = inventario_inicial + producto_recibido
inventario_actual= suma - producto_vendido
print(f"""Inventario inicial: {inventario_inicial:>10}
Productos recibidos: {producto_recibido:>10}
Productos vendidos: {producto_vendido:>10}
Inventario actual: {inventario_actual:>10}""")

