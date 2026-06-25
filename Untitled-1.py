cliente = input("Ingrese el nombre del cliente: ")
dias_estancia = int(input("ingrese la cantidad de dias de estancia: "))
tarifa_diaria = float(input("ingrese la tarifa diaria la reserva: "))
habitacion_con_vista_mar = input("la habitacion posee vista al mar (Si/No): ").lower()

tarifa_final= dias_estancia * tarifa_diaria

if habitacion_con_vista_mar == "si":
   
    print("Habitación con vista al mar")
else:
    
    print("Habitación sin vista al mar")

print(f''' ticket de reserva
      nombre: {cliente},
      dias de estancia: {dias_estancia},
      valor estancia:  {tarifa_final},
      habitacion con vista al mar: {habitacion_con_vista_mar}

''')