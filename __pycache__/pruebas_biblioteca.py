from biblioteca import Biblioteca

biblioteca1 = Biblioteca("Biblioteca Nacional de Colombia")

while True:
    print(f'''**Biblioteca Nacional de Colombia**
          
          1.agregar libro
          2.buscar por autor
          3.buscar por titulo
          4.buscar por genero
          5.mostrar todos los libros
          6.salir
''')
    opcion = int(input('ingrese la opcion que desea: '))

    if opcion == 1:
        titulo = input('ingrese el titulo del libro: ')
        autor = input('ingrese el autor del libro: ')
        genero = input('ingrese el genero del libro: ')
        biblioteca1.agregar_libro(titulo,autor,genero)
        print('libro agregado correctamente...\n')

    elif opcion == 2:
        autor = input('ingrese el nombre del autor: ').strip().lower()
        biblioteca1.buscar_libro_autor(autor)
    elif opcion == 3:
        titulo = input('ingrese el titulo del libro: ').strip().lower()
        biblioteca1.mostrar_libro(titulo)
    elif opcion == 4:
        genero = input('ingrese el genero del libro: ').strip().lower()
        biblioteca1.buscar_por_genero(genero)
    elif opcion == 5:
        biblioteca1.mostrar_todos_los_libros()
    elif opcion == 6:
        print('hasta luego')
        break
    else:
        print('opcion no validad..')

    
