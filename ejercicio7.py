salir = True

while salir:
    print(f'''menu:
          1.crear cuenta
          2.eliminar cuenta
          3.salir''')
    
    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        print("creando cuenta...")
    elif opcion == 2:
        print("eliminando cuenta...")
    elif opcion == 3:
        print("saliendo del menu...")
        break
    else:
        print("opcion no valida..")