import hashlib

usuario1 = "daniel"
# La contraseña se guarda como hash, nunca en texto plano
contraseña1_hash = hashlib.sha256("celeste1907".encode()).hexdigest()

intentos = 3

while intentos > 0:
    usuario = input("ingrese su usuario: ")
    contraseña = input("ingrese su contraseña: ")
    
    # Convertimos lo que escribió el usuario a hash y comparamos
    contraseña_hash = hashlib.sha256(contraseña.strip().encode()).hexdigest()
    
    if usuario.strip() == usuario1 and contraseña_hash == contraseña1_hash:
        print("acceso correcto")
        break
    else:
        intentos -= 1
        print(f"acceso denegado. intentos restantes: {intentos}")

if intentos == 0:
    print("cuenta bloqueada")