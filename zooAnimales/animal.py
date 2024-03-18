class Animal:
    #Attributes
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    #Getters and Setters
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona
    
    #Methods
    def movimiento(self):
        return "desplazarse"
    
    def totalPorTipo(self):
        return f"Mamiferos: {getattr(globals().Mamifero.cantidadMamiferos())()}\nAves: {getattr(globals().Ave.cantidadAves())()}\nReptiles: {getattr(globals().Reptil.cantidadReptiles())()}\nPeces: {getattr(globals().Pez.cantidadPeces())()}\nAnfibios: {getattr(globals().Anfibio.cantidadAnfibios())()}"
    #{Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}
    
    def __str__(self):
        if self._zona == None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.getZoologico()}"