from zooAnimales.animal import Animal

class Pez (Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre,edad,habitat,genero,None)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color_colorEscamas):
        self._colorEscamas = color_colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,cantidad_cantidadAletas):
        self._cantidadAletas = cantidad_cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)

    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones += 1
        salmon = Pez(nombre,edad,"oceano",genero,"rojo",6)
        Pez._listado.append(salmon)

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.bacalaos += 1
        bacalaos = Pez(nombre,edad,"oceano",genero,"gris",6)
        Pez._listado.append(bacalaos)