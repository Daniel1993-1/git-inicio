from manejo_archivo2 import ServicioSnack
from manejo_archivos import Snack
class MaquinaSnacks:
    def __init__(self):
        self.servicios_snacks = ServicioSnack()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('*** maquina de snacks ***')
        self.servicios_snacks.mostrar_snack()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'ocurrio un error: {e}')


    def mostrar_menu(self):
        print(f'''menu:
        1. comprar snack
        2. mostrar ticket
        3. agregar nuevo snack al inventario
        4. inventario snacks
        5.3 salir''')
        return int(input('elige una opcion: '))

    def ejecutar_opcion(self,opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicios_snacks.mostrar_snack()
        elif opcion == 5:
            print('regresa pronto!')
            return True
        else:
            print(f'opcion invalida. {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('que snack quieres comprar (id): '))
        snacks = self.servicios_snacks.get_snack()

        snack = next((snack for snack in snacks if snack.id_snack == id_snack),None)
        if snack:
            self.productos.append(snack)
            print(f'snack encontrado: {snack}')
        else:
            print(f'id snack no encontrado: {id_snack}')

    def mostrar_ticket(self):
        if not self.productos:
            print('no hay snacks en el ticket')
            return
        total = sum(snack.precio for snack in self.productos)
        print('---ticket de venta---')
        for producto in self.productos:
            print(f'\t- {producto.nombre}- ${producto.precio:2.f}')
        print(f'\ttotal -> ${total:2f}')

    def agregar_snack(self):
        nombre = input('nombre del snack: ')
        precio = float(input('precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicios_snacks.agregar_snack(nuevo_snack)
        print('snack agregado correctamente')

if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()