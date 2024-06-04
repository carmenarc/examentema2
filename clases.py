class Empleado:
    def __init__(self, nombre, edad, salario_anual):
        self._nombre = nombre
        self._edad = edad
        self._salario_anual = salario_anual
 
    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
 
    @property
    def edad(self):
        return self._edad
 
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
 
    @property
    def salario_anual(self):
        return self._salario_anual
 
    @salario_anual.setter
    def salario_anual(self, nuevo_salario):
        self._salario_anual = nuevo_salario
 
    def calcular_salario_mensual(self):
        return self._salario_anual / 12
 
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_anual, bono):
        super().__init__(nombre, edad, salario_anual)
        self._bono = bono
 
    @property
    def bono(self):
        return self._bono
 
    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono
 
    def calcular_salario_mensual(self):
        salario_base_mensual = super().calcular_salario_mensual()
        return salario_base_mensual + self._bono / 12
class Empleado:
    def __init__(self, nombre, edad, salario_anual):
        self._nombre = nombre
        self._edad = edad
        self._salario_anual = salario_anual
 
    @property
    def nombre(self):
        return self._nombre
 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
 
    @property
    def edad(self):
        return self._edad
 
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
 
    @property
    def salario_anual(self):
        return self._salario_anual
 
    @salario_anual.setter
    def salario_anual(self, nuevo_salario):
        self._salario_anual = nuevo_salario
 
    def calcular_salario_mensual(self):
        return self._salario_anual / 12
 
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_anual, bono):
        super().__init__(nombre, edad, salario_anual)
        self._bono = bono
 
    @property
    def bono(self):
        return self._bono
 
    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono
 
    def calcular_salario_mensual(self):
        salario_base_mensual = super().calcular_salario_mensual()
        return salario_base_mensual + self._bono / 12
