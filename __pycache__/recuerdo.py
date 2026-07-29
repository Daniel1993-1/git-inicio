class Pelicula:
    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre



class ServicioPeliculas:
    Nombre_archivo = 'catalogo.txt'

    def __init__(self):
        self.lista_peliculas = []


    def agregar_pelicula(self,nombre):
        pelicula = Pelicula(nombre)
        self.lista_peliculas.append(pelicula.nombre)
        

    def obtener_lista(self):
        for i, pelicula in enumerate(self.lista_peliculas, start=1):
            print(f"{i}. {pelicula}")

    def eliminar_lista(self):
        self.lista_peliculas.clear()

    def guardar_en_archivo(self):
        try:
            with open(self.Nombre_archivo,'w') as archivo:
                for pelicula in self.lista_peliculas:
                    archivo.write(pelicula + '\n')
                print('catalogo guardado')
        except Exception as e:
            print(f'ocurrio un erro {e}')

    def cargar_desde_archivo(self):
        try:
            with open(self.Nombre_archivo, 'r') as archivo:
                self.lista_peliculas = [linea.strip() for linea in archivo.readlines()]
            print("catálogo cargado")
        except FileNotFoundError:
            print("no existe archivo, empezando catálogo nuevo")

if __name__ == '__main__':

    servicio = ServicioPeliculas()
    servicio.cargar_desde_archivo()
    salir = True

    while salir:

        print(f'''**catalogo peliculas**
            1. agregar pelicula
            2. listar peliculas
            3. eliminar catalogo
            4. salir..''')

        try:
            opcion = int(input('ingrese la opcion que desea: '))
            if opcion ==1:
                nombre = input("Nombre de la película: ")
                servicio.agregar_pelicula(nombre)
                servicio.guardar_en_archivo()
            elif opcion ==2:
                servicio.obtener_lista()
            elif opcion == 3:
                servicio.eliminar_lista()
                servicio.guardar_en_archivo()
                print("Catálogo eliminado.")
            elif opcion ==4:
                print('saliendo del catalogo..')
                salir = False
            else:
                print('opcion no valida!')
        except Exception as e:
            print(f'ocurrio un error {e}')