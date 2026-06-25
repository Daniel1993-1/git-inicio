compra = int(input("ingrese el valor de la compra: "))
membresia = input("posee membresia de la tienda: ").strip().lower()
MINIMO_DESCUENTO = 1000

if compra >= MINIMO_DESCUENTO and membresia == "si":
    descuento = compra * 0.1
elif compra >= MINIMO_DESCUENTO and membresia == "no":
    descuento = compra * 0.05
else:
    descuento = 0

compra_final = compra - descuento

print(f"""--- ticket de compra ---
compra:             ${compra}
descuento:          ${descuento}
valor con descuento: ${compra_final}
""")