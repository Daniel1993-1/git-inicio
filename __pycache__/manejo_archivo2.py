import os.path
from manejo_archivos import Snack

class ServicioSnack:
    NOMBRE_ARCHIVO ='snack.txt'


    def __init__(self):
        self.snacks = []

        #revisar si ya existe el archivo snack
        #si ya existe, obtenemos los snack del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        #sino,cargamos algunos snack iniciales
        else:
            self.cargar_snack_iniciales()

    def cargar_snack_iniciales(self):
        snacks_iniciales = [
            Snack('papas',70),
            Snack('refresco',50),
            Snack('sandwich',120)
            
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snack_archivo(snacks_iniciales)

    def guardar_snack_archivo(self,snacks):
        try:
            with open(self.NOMBRE_ARCHIVO,'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en el archivo')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r')as archivo:
                for linea in archivo:
                    id_snack,nombre,precio = linea.strip().split(',')
                    snack = Snack(nombre,float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f' error al leer archivo de snacks: {e}')
        return snacks

    def agregar_snack(self,snack):
        self.snacks.append(snack)
        self.guardar_snack_archivo([snack])

    def mostrar_snack(self):
        print('---snacks en el inventario---')
        for snack in self.snacks:
            print(snack)

    def get_snack(self):
        return self.snacks