from clases import Empleado

class Empresa:

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []
    
    def contratar_empleado(self,nombre,departamento):
        empleado = Empleado(nombre,departamento)
        self.empleados.append(empleado)

    def obtener_empleados(self,departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1 
        return contador_empleados_por_departamento       
    
    def obtener_total_empleados(self):
        print(f'\n total empleados para la empresa: {self.nombre}')
        for empleado in self.empleados:
            print(f'''empleado {empleado.id}
                nombre: {empleado.nombre}
                departamento: {empleado.departamento}
''')