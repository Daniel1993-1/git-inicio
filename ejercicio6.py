USUARIO = "admin"
CONTRASEÑA = "celeste1907"

usuario = input("ingrese su usuario: ")
contraseña = input("ingrese su contraseña: ")

if usuario == USUARIO and CONTRASEÑA == "celeste1907":
    print("ingreso exitoso..")

elif usuario == USUARIO  and CONTRASEÑA != "celeste1907":
    print("contraseña incorrecta...")

elif usuario != USUARIO  and CONTRASEÑA =="celeste1907":
    print("usuario incorrecto")

else:
    print("usuario y contraseña incorrecta...")