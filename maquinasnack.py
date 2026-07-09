maquina = []
compras = []

def agregar_snack():
    nombre = input('ingresa el nombre del snack: ')
    cantidad = int(input('ingresa la cantidad del snack: '))
    precio = float(input('ingresa el precio del snack: '))
    nuevo_snack = {'id': len(maquina) + 1, 'nombre': nombre,'cantidad': cantidad,'precio': precio}
    maquina.append(nuevo_snack)

def mostrar_snack():
    if len(maquina) == 0:
        print('maquina vacia.')
    for snack in maquina:
        
        print(f'''
              id:{snack.get('id')},
              nombre:{snack.get('nombre')},
              cantidad:{snack.get('cantidad')},
              precio:{snack.get('precio')}

''')

def comprar_snack():
    
    compra = int(input('ingrese el id del snack: '))
    encontrado = False
    
    for snack in maquina:
         if snack.get('id') == compra:
            compra = {
                "id": snack["id"],
                "nombre": snack["nombre"],
                "precio": snack["precio"]
}
            compras.append(snack)
            print('snack comprado.')
            encontrado = True
            break
    if not encontrado:
        print("Snack no disponible.") 

def mostrar_ticket():
    precio_final = 0

    print("====== TICKET DE COMPRA ======")
    
    for snack in compras:
        
        
        print(f'''ticket de compra
              id:{snack.get('id')},
              nombre:{snack.get('nombre')},
              precio:{snack.get('precio')},
              ''')    
        
        precio_final += snack.get('precio')

    print(f"TOTAL A PAGAR: ${precio_final:,.0f}")

            
            
            

if __name__ == "__main__":

    while True:
        print(f'''maquina de snack
              
              1.agregar snack
              2.comprar snack
              3.mostrar ticket de compra
              4.mostrar snaks
              5.salir
''')
        opcion = int(input('ingrese la opcion que desea: '))

        if opcion == 1:
            agregar_snack()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            mostrar_snack()
        elif opcion == 5:
            
            break
        else:
            print('ingrese una opcion valida..')