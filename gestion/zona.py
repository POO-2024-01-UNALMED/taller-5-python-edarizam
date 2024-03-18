class Zona:
    def __init__(self, nombre, zoologico = None, animales = None):
        self._nombre = nombre
        self._zoologico = zoologico
        self._animales = animales
    
    #Getters and Setters
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoologico(self):
        return self._zoologico
    
    def setZoologico(self, zoologico):
        self._zoologico = zoologico
    
    def getAnimales(self):
        return self._animales
    
    def setAnimales(self, animales):
        self._animales = animales

    #Methods
    def agregarAnimales(self, animal):
        if self._animales == None:
            self._animales = []
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        if self._animales == None:
            return 0
        return len(self._animales)