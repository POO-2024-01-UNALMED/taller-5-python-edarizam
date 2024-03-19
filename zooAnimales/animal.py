class Animal:
    #Attributes
    _totalAnimales = 0
    animales = []
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1
        Animal.animales.append(self)

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
    
    @classmethod
    def getMamifero(cls):
        for animal in Animal.animales:
            try:
                if animal.caballos >= 0:
                    return animal
            except: continue
        return 0
    
    @classmethod
    def getPez(cls):
        for animal in Animal.animales:
            try:
                if animal.bacalaos >= 0:
                    return animal
            except: continue
        return 0
    
    @classmethod
    def getReptil(cls):
        for animal in Animal.animales:
            try:
                if animal.serpientes >= 0:
                    return animal
            except: continue
        return 0
    
    @classmethod
    def getAve(cls):
        for animal in Animal.animales:
            try:
                if animal.halcones >= 0:
                    return animal
            except: continue
        return 0
    
    @classmethod
    def getAnfibio(cls):
        for animal in Animal.animales:
            try:
                if animal.salamandras >= 0:
                    return animal
            except: continue
        return 0
    
    #Methods
    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos : {Animal.getMamifero().cantidadMamiferos()}\nAves : {Animal.getAve().cantidadAves()}\nReptiles : {Animal.getReptil().cantidadReptiles()}\nPeces : {Animal.getPez().cantidadPeces()}\nAnfibios : {Animal.getAnfibio().cantidadAnfibios()}"
    #{Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}
    
    def toString(self):
        if self._zona == None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.getZoologico()}"