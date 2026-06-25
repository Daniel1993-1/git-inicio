nombre_producto = input("ingrese el nombre del producto: ")
precio_producto = float(input("ingrese el precio del producto: "))
cantidad_en_el_inventario = int(input("cantidad en el inventario: "))


if cantidad_en_el_inventario == 0:
    producto_disponible= "producto no disponible...."
   
else:
    producto_disponible= f'producto disponible en inventario ({cantidad_en_el_inventario})'

print(f''' ticket de compra 
        nombre producto: {nombre_producto},
        precio del producto: {precio_producto},
        cantidad en el inventario: {cantidad_en_el_inventario},
        producto disponible: {producto_disponible}



''')