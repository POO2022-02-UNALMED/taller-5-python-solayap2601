class Zoologico():

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self, zona):
        self_zonas.append(zona)

    def cantidadTotalAnimales(self):
        a=0
        for i in self._zonas:
            a += i.cantidadAnimales()   
        return a
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicación(self, ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas

    def setZonas(self, zonas):
        self._zonas = zonas
