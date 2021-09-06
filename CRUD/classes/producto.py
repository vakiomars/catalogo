# Se crea la clase producto para guardar los partametros que vamos a capturar de la clase producto
# Self siempre siempre se coloca de primero en el cosntructor y en cualquier método qe definamos
# en una clase en python
# Se añade seguidamente los campos que se quieren guardar y se asignan a las variables de la clase
# que seran de tipo privada, esto se define añadiendo un _ al inicio del nobmre de la variable. 

class Producto:

    def __init__(self, codigoProducto, nombreProducto, descripcionProducto, tipoProducto, saborProducto, 
    marca, presentacion, gramaje, valor):
        self._codigoProducto = codigoProducto
        self._nombreProducto = nombreProducto
        self._descripcionProducto = descripcionProducto
        self._tipoProducto = tipoProducto
        self._saborProducto = saborProducto
        self._marca = marca
        self._presentacion = presentacion
        self._gramaje = gramaje
        self._valor = valor

# Se definen los constructores y los modificadores

    @property
    def codigoProducto(self):
        return self._codigoProducto
    
    @codigoProducto.setter
    def codigoProducto(self, codigoProducto):
        self._codigoProducto = codigoProducto
    
    @property
    def nombreProducto(self):
        return self._nombreProducto
    
    @nombreProducto.setter
    def nombreProducto(self, nombreProducto):
        self._nombreProducto = nombreProducto

    @property
    def descripcionProducto(self):
        return self._descripcionProducto
    
    @descripcionProducto.setter
    def descripcionProducto(self, descripcionProducto):
        self._descripcionProducto = descripcionProducto

    @property
    def tipoProducto(self):
        return self._tipoProducto

    @tipoProducto.setter
    def tipoProducto(self, tipoProducto):
        self._tipoProducto = tipoProducto

    @property
    def saborProducto(self):
        return self._saborProducto

    @saborProducto.setter
    def saborProducto(self, saborProducto):
        self._saborProducto = saborProducto

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def presentacion(self):
        return self._presentacion

    @presentacion.setter
    def presentacion(self, presentacion):
        self._presentacion = presentacion

    @property
    def gramaje(self):
        return self._gramaje

    @gramaje.setter
    def gramaje(self, gramaje):
        self._gramaje = gramaje

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor
