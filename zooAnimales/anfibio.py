from zooAnimales.animal import Animal

class Anfibio (Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre,edad,habitat,genero,None)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    
    def isVenenoso(self,venenoso):
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        Anfibio.ranas += 1
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio._listado.append(rana)

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio._listado.append(salamandra)