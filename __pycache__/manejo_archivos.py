nombre_archivo = 'mi_archivo_txt'
try:
    with open(nombre_archivo,'x') as archivo:
        archivo.write('hola como estas modo exclusivo')
        archivo.write('\nse agrega informacion al archivo\n')
except FileExistsError as e:
    print(f'el archivo {nombre_archivo} ya existe')
    print(f'detalle del error {e}')


with open(nombre_archivo,'a')as archivo:
    archivo.write('anexando informacion..\n')
    archivo.write('nueva informacion\n')


with open(nombre_archivo,'r') as archivo:
    print(archivo.read())