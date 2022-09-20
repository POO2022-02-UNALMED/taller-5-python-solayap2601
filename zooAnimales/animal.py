from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal:

    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    @staticmethod
    def movimiento(self):
        return 'desplazarse'

    def totalPorTipo():
        return 	"Mamiferos : " + str(Mamifero.cantidadMamiferos()) +'\nAves : ' +str(Ave.cantidadAves()) + '\nReptiles : '+str(Reptil.cantidadReptiles()) +'\nPeces : '+str(Pez.cantidadPeces()) +'\nAnfibios : '+str(Anfibio.cantidadAnfibios())
        
    def toString(self):
        pres = 'Mi nombre es ' + self._nombre + ', tengo una edad de ' + str(self._edad) + ',habito en ' + self._habitad + 'y mi genero es ' + self._genero;
        if self._zona != None:
            pres += ', la zona en la que me ubico es ' + self._zona + ', en el ' + self._zona.getZoo()
        return pres   

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

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona
      
