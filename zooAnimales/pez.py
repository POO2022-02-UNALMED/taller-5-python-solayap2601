from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        Pez._listado.append(self)
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._zona = None

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @staticmethod
    def movimiento():
        return 'nadar'

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, 'oceano' , genero, 'rojo', 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, 'oceano' , genero, 'gris', 6 )
    
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
        self._habitad = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona
