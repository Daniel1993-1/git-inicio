class DispositivoEntrada:

    def __init__(self,marca,tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada
    
class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_ratones = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'id: {self.id_ratones} marca: {self.marca} - tipo de entrada: {self.tipo_entrada}'
    
class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f'id: {self.id_teclado} - marca: {self.marca} - tipo entrada: {self.tipo_entrada}'

if __name__ == '__main__':

    raton1 = Raton('hp','usb')
    print(raton1)
    raton2 = Raton('acer','bluethoo')
    print(raton2)
    teclado1 = Teclado('samsung', ' inalambrico')
    print(teclado1)
    teclado2 = Teclado('compumax','wifi')
    print(teclado2)
        