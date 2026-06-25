import secrets #mas seguro y posee otros metodos 

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
año_nacimiento = int(input("ingrese su año de nacimiento: "))
numero_aleatorio = secrets.randbelow(10000)


id_unico = f'{nombre.strip().upper()[0:2]}{apellido.strip().upper()[0:2]}{str(año_nacimiento)[2:]}{numero_aleatorio}'

print(id_unico)

# Token hexadecimal (como los de sesiones web)
token = secrets.token_hex(16)
print(token)  # → "a3f8c2d1e4b7a9f0c3d2e1b4a8f7c6d5"

# Token en base64 (URLs seguras)
url_token = secrets.token_urlsafe(16)
print(url_token)  # → "X7kP2mQnR4sT8vWx"

# Número aleatorio seguro
numero = secrets.randbelow(10000)
print(numero)  # → 4821