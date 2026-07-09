from libro import Libro

class Biblioteca:

    def __init__(self,nombre):
        self._nombre = nombre
        self.libros = []
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    def agregar_libro(self,titulo,autor,genero):
        agregar = Libro(titulo,autor,genero)
        self.libros.append(agregar)

    def buscar_libro_autor(self,autor):
        encontrado = False
        for encontrar in self.libros:
            if encontrar.autor == autor:
                print(f'''libro encontrado
                      titulo : {encontrar.titulo},
                      autor : {encontrar.autor},
                      genero : {encontrar.genero}''')
                encontrado = True
        if not encontrado:
            print(f'el libro no se encuentra en la biblioteca {self.nombre}')
    
    def buscar_por_genero(self,genero):
        encontrado = False
        for encontrar in self.libros:
            if encontrar.genero == genero:
                print(f'''libro encontrado
                      titulo : {encontrar.titulo},
                      autor : {encontrar.autor},
                      genero : {encontrar.genero}''')
                encontrado = True
        if not encontrado:
            print(f'el libro no se encuentra en la biblioteca {self.nombre}')
        
    def mostrar_todos_los_libros(self):
        if len(self.libros) == 0:
            print('la biblioteca esta vacia.\n')
            return
            
        print(f"\nBiblioteca: {self.nombre}")
        print("-" * 30)

        for libro in self.libros:
            print(f'''
                titulo:{libro.titulo}
                autor: {libro.autor}
                genero:{libro.genero}''')
    
    def mostrar_libro(self,titulo):
        encontrado = False
        for encontrar in self.libros:
            if encontrar.titulo == titulo:
                print(f'''
                titulo:{encontrar.titulo}
                autor: {encontrar.autor}
                genero:{encontrar.genero}''')
                encontrado = True
                break
        if not encontrado:
            print(f'el libro no se encuentra en la biblioteca {self.nombre}')


