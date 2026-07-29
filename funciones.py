inventario = []

salir = False


def agregar_producto():
    agregar = int(input('ingrese la cantidad de productos para agregar al inventario: '))

    for i in range(agregar):
        nombre = input('ingrese el nombre del producto: ')
        cantidad = int(input('ingrese la cantidad del producto: '))
        precio = float(input('ingrese el precio del producto: '))
        print()
        nuevo_producto = {'id': len(inventario) + 1,'nombre':nombre, 'cantidad':cantidad, 'precio':precio}
        inventario.append(nuevo_producto)

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
        print()
        return
    for producto in inventario:
        print(f'''--detalle del inventario--
              ID:{producto.get('id')},
              Nombre:{producto.get('nombre')},
              Cantidad:{producto.get('cantidad')},
              Precio: {producto.get('precio')}''')

def buscar_producto():
    buscar_id=int(input('ingrese el id del producto a buscar: '))
    encontrado = False
    for producto in inventario:
        if producto.get('id') == buscar_id:
            print(f'''--detalle del producto--
                  id:{producto.get('id')},
                  nombre:{producto.get('nombre')},
                  cantidad:{producto.get('cantidad')},
                  precio:{producto.get('precio')}
                ''')
            encontrado = True
            break

    if not encontrado:
        print(f"No existe un producto con el ID {buscar_id}.")


while not salir:
    print(f'''---Inventario---
          1.Mostrar el inventario
          2.Agregar nuevo producto
          3.Buscar producto por ID
          4.Salir
''')
    opcion = int(input('ingrese la opcion que desea: '))

    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        
        print('saliendo del programa..')
        salir = True
    else:
        print('opcion no validad...')




