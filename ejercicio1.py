nombre = input("ingrese su usuario: ")
pasos_caminados_en_el_dia = int(input("ingrese la cantidad de pasos: "))

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

calorias_quemadas = pasos_caminados_en_el_dia * CALORIAS_POR_PASO
if pasos_caminados_en_el_dia >= META_PASOS_DIARIOS:
    mensaje = "LOGRASTE LA META DIARIA"
else:
    mensaje = "NO LOGRASTE LA META DIARIA ANIMO..."

#mensaje = "LOGRASTE LA META DIARIA" if pasos_caminados_en_el_dia >= META_PASOS_DIARIOS else "NO LOGRASTE LA META DIARIA, ÁNIMO..."

print(f'''---resumen del dia---
      nombre = {nombre}
      pasos en el dia = {pasos_caminados_en_el_dia},
      calorias quemadas = {calorias_quemadas:.1f},
      meta diaria = {META_PASOS_DIARIOS}
      resumen del dia = {mensaje}
''')