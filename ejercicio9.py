contraseña = input("ingrese su contraseña: ")

while len(contraseña) < 6:
    print("la contraseña debe tener mas de 6 caracteres")
    contraseña = input("ingrese su contraseña: ")
    print("creacion de contraseña exitoso.")