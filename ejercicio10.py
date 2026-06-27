suscripciones = {"daniel@gmail.com","celeste@gmail.com"}

nueva_suscripcion = input("ingrese su correo para la suscripcion: ").strip().lower()

if nueva_suscripcion in suscripciones:
    print("el correo ya se encuentra inscrito...")
else:
    suscripciones.add(nueva_suscripcion)
    print("su suscripcion a sido exitosa..")

print('\n----lista de suscripciones---')

for suscritos in suscripciones:
    print(suscritos)