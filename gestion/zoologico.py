class Zoologico:
    #Attributes
    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
    
    #Getters and Setters
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZonas(self):
        return self._zonas
    
    def setZonas(self, zonas):
        self._zonas = zonas
    
    #Methods
    def agregarZonas(self, zonas):
        if self._zonas == None:
            self._zonas = []
        self._zonas.append(zonas)
    
    def cantidadTotalAnimales(self):
        totalAnimales = 0
        if self._zonas == None:
            return 0
        for zona in self._zonas:
            totalAnimales += len(zona.getAnimales())
