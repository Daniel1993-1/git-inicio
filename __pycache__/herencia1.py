from herencia import Teclado,Raton


class Monitor:
    contador_monitores = 0

    def __init__(self,marca,tamaño):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamaño = tamaño

    def __str__(self):
        return f'id:{self.id_monitor} - marca: {self.marca} - tamaño: {self.tamaño}'

class Computadora:
    contador_computadoras = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self.id_computadoras = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        
    def __str__(self):
        return f'''{self.nombre}: {self.id_computadoras}
        monitor: {self.monitor}
        teclado: {self.teclado}
        raton: {self.raton}
'''
class Orden:
    contador_ordenes = 0
    

    def __init__(self,computadoras):
        Orden.contador_ordenes += 1
        self.id_ordenes = Orden.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self,computadoras):
        self.computadoras.append(computadoras)
    
    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'''Orden {self.id_ordenes}
        Computadoras: {computadoras_str}'''

if __name__ == '__main__':
    
    

    print('*' * 20)
    monitor1 = Monitor('hp',42)
    teclado1 = Teclado('hp','wifi')
    raton1 = Raton('acer','usb')
    computadora1 = Computadora('nesus',monitor1,teclado1,raton1)

    print(computadora1)

    print('*' * 20)
    monitor2 = Monitor('hp',42)
    teclado2 = Teclado('hp','wifi')
    raton2 = Raton('acer','usb')
    computadora2 = Computadora('compumax',monitor2,teclado2,raton2)

    print(computadora2)

    orden1 = Orden()

