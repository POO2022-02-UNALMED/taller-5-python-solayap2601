from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        Mamifero._listado.append(self)
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas
        self._zona = None

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera" , genero, True , 4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "selva" , genero, True , 4)

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas
    
    def isPelaje(self):
        return self._pelaje

