saldo = 1000
salir = True

while salir:
    print(f'''--menu--
          1.depositar
          2.retirar
          3.consultar saldo
          4.salir
''')
    opcion = int(input("ingrese la opcion que desea realizar: "))

    if opcion == 1:
        deposito = int(input("ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f'su deposito a sido exitoso su saldo actual es de ${saldo:,.0f}\n')
        else:
            print("el deposito debe ser mayor de 0")
        
    elif opcion == 2:
        retiro = int(input("ingrese el monto a retirar: "))
        if retiro <= 0:
            print("el retiro deber ser mayor de 0")
        elif saldo < retiro:
            print(f'tu saldo es insuficiente su saldo es de ${saldo:,.0f}\n')
        
        else:
            saldo -= retiro
            print(f'tu retiro fue exitoso su saldo actual es de ${saldo:,.0f}\n')
    elif opcion == 3:
        print(f"Su saldo actual es: ${saldo:,.0f}\n")
    elif opcion == 4:
        print("saliendo del cajero...")
        salir = False
    else:
        print("opcion no valida...")