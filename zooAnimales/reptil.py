from zooAnimales.animal import Animal

class Reptil (Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre,edad,habitat,genero,None)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self,largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        Reptil.iguanas += 1
        iguana = Reptil(nombre,edad,"humedal",genero,"verde",3)
        Reptil._listado.append(iguana)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        Reptil.serpientes += 1
        serpiente = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        Reptil._listado.append(serpiente)