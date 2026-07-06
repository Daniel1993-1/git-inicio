productos = [
    {'id':1,'nombre':'arroz','cantidad':12,'precio':120},
    {'id':2,'nombre':'aceite','cantidad':8,'precio':150},
    {'id':3,'nombre':'cafe','cantidad':4,'precio':80},
]
producto_nuevo= int(input('ingresa la cantidad de productos a ingresar:'))

for i in range (producto_nuevo):
    nombre=input('nombre del producto: ')
    precio=float(input('ingrese el precio: '))
    cantidad = int(input('ingrese la cantidad del producto: '))
    nuevo_ingreso={'id': len(productos) +1 ,'nombre':nombre,'cantidad':cantidad,'precio':precio}
    productos.append(nuevo_ingreso)

print(productos)

buscar_id = int(input('ingrese el id a buscar: '))

encontrado = False

for producto in productos:
    if producto['id'] == buscar_id:
        print(f'''
--- DETALLE DEL PRODUCTO ---
ID: {producto['id']}
Nombre: {producto['nombre']}
Cantidad: {producto['cantidad']}
Precio: ${producto['precio']}
''')
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")
        