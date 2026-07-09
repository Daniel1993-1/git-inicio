from clases import Empleado
from clases1 import Empresa

print('pruebas de sistema de empleados')


empresa1 = Empresa('NOEL')

empresa1.contratar_empleado('daniel','ventas')
empresa1.contratar_empleado('susana','compras')
empresa1.contratar_empleado('karen','produccion')

Empleado.obtener_total_empleados()
empresa1.obtener_total_empleados()